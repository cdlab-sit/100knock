''' 動詞の格パターンの抽出 '''
# 今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
# 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
# ただし，出力は以下の仕様を満たすようにせよ．
#  動詞を含む文節において，最左の動詞の基本形を述語とする
#  述語に係る助詞を格とする
#  述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
import re
import CaboCha

# python


def main():
    file_name = 'neko.txt.cabocha'
    neko_txt_cabocha = read_file(file_name)
    sentence_list = load_dependency_parsing(neko_txt_cabocha)
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


def extract_verb_case_pattern(sentences):
    f = open('extract_verb_case_pattern.txt', 'w')
    for chunks in sentences:
        for chunk in chunks:
            pos_list = chunk.get_pos()
            if '動詞' in pos_list:
                pos_index = pos_list.index('動詞')
                srcs_list = chunk.srcs
                particle_auxiliary_verbs = sorted(  # [-1]じゃないほうがいいけどモチベがあがらん
                    [chunks[srcs].morphs[-1].surface for srcs in srcs_list])
                f.write(f'{chunk.morphs[pos_index].base}\t\
{" ".join(particle_auxiliary_verbs)}\n')
    f.close()

if __name__ == "__main__":
    main()

# UNIX
# sort extract_verb_case_pattern.txt | uniq --count | sort --numeric-sort
# --reverse > "all.txt"

# grep "^する\s" extract_verb_case_pattern.txt | sort | uniq --count
# | sort --numeric-sort --reverse > "suru.txt"
