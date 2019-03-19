''' 機能動詞構文のマイニング '''
# 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
# 46のプログラムを以下の仕様を満たすように改変せよ．
#  「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
#  述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
#  述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
#  述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）

import re
import CaboCha


def main():
    input_line = input('動詞の格パターンの抽出したい文章を入力してください\n:')
    input_line_cabocha = dependency_parsing(input_line)
    sentence_list = load_dependency_parsing(input_line_cabocha)
    extract_verb_case_pattern(sentence_list)


def dependency_parsing(sentence):
    c = CaboCha.Parser()
    analysis_results = []
    for line in sentence.split('\n'):
        tree = c.parse(line)
        analysis_results.append(tree.toString(CaboCha.FORMAT_XML))
    return '\n'.join(analysis_results)


def read_file(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()
    return contents


def load_dependency_parsing(analytical_data):
    sentence_pattern = r"<sentence>(.+?)</sentence>"
    chunk_pattern = r'<chunk id="(\d*)" link="(.+?)"(.+?)</chunk>'
    morpheme_pattern = r'<tok id="\d*" feature="(.+?),(.+?),' \
                       '.+?,.+?,.+?,.+?,(.+?),.+?>(.+?)</tok>'
    sentences = re.findall(sentence_pattern, analytical_data, flags=re.DOTALL)
    sentence_list = []
    for sentence in sentences:
        chunks = re.findall(chunk_pattern, sentence, flags=re.DOTALL)
        chunk_class_list = []
        srcs_dic = {}
        for chunk in chunks:
            morphemes = re.findall(morpheme_pattern, chunk[2], flags=re.DOTALL)
            morph_class_list = []
            for morpheme in morphemes:
                m = Morph(surface=morpheme[3], base=morpheme[2],
                          pos=morpheme[0], pos1=morpheme[1])
                morph_class_list.append(m)
                srcs_dic.setdefault(int(chunk[0]), chunk[1])
            srcs = [k for k, v in srcs_dic.items() if v == chunk[0]]
            c = Chunk(morphs=morph_class_list, dst=chunk[1], srcs=srcs)
            chunk_class_list.append(c)
        sentence_list.append(chunk_class_list)
    return sentence_list


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def get_morph(self):
        return f'surface = {self.surface}\tbase = {self.base}\t\
pos = {self.pos}\tpos1 = {self.pos1}'


class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = int(dst)
        self.srcs = srcs

    def get_elements(self):
        return f'morphs[{self.get_phrase()}]\t\
dst[{self.dst}]\tsrcs = {self.srcs}'

    def get_phrase(self):
        show_morphs = []
        for morph in self.morphs:
            if morph.pos != '記号':
                show_morphs.append(morph.surface)
        return ''.join(show_morphs)

    def get_pos(self):
        return [morph.pos for morph in self.morphs]

    def get_pos1(self):
        return [morph.pos1 for morph in self.morphs]


def extract_verb_case_pattern(sentences):
    f = open('extract_verb_frame_info.txt', 'w')
    for chunks in sentences:
        for chunk in chunks:
            for i, morph in enumerate(chunk.morphs):
                if morph.pos == '名詞' and morph.pos1 == 'サ変接続' and \
                   chunk.morphs[i+1] and chunk.morphs[i+1].surface == 'を' and\
                   chunk.morphs[i+1].pos == '助詞' and \
                   '動詞' in chunks[chunk.dst].get_pos():
                    print(f'{chunk.get_phrase()}{chunks[chunk.dst].get_phrase()}')
                    srcs_list = chunks[chunk.dst].srcs
                    particle_auxiliary_verbs = sorted(
                        [chunks[srcs].morphs[-1].surface for srcs in srcs_list])
                    phrases = sorted(
                        [chunks[srcs].get_phrase() for srcs in srcs_list])
                    print(f'{" ".join(particle_auxiliary_verbs)}\t{" ".join(phrases)}\n')
    f.close()

if __name__ == "__main__":
    main()
