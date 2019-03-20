''' 名詞間の係り受けパスの抽出 '''
# 文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
# ただし，名詞句ペアの文節番号がiとj（i<j）のとき，係り受けパスは以下の仕様を満たすものとする．
#  問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現（表層形の形態素列）を
#   "->"で連結して表現する
#  文節iとjに含まれる名詞句はそれぞれ，XとYに置換する
# また，係り受けパスの形状は，以下の2通りが考えられる．
#  文節iから構文木の根に至る経路上に文節jが存在する場合: 文節iから文節jのパスを表示
#  上記以外で，文節iと文節jから構文木の根に至る経路上で共通の文節kで交わる場合:
#  文節iから文節kに至る直前のパスと文節jから文節kに至る直前までのパス，文節kの内容を"|"で連結して表示
import re
import CaboCha


def main():
    input_line = input('グラフにしたい文を入力してください\n:')
    input_line_cabocha = dependency_parsing(input_line)
    sentence_list = load_dependency_parsing(input_line_cabocha)
    make_received_relates_pass(sentence_list)


def dependency_parsing(sentence):
    c = CaboCha.Parser()
    analysis_results = []
    for line in sentence.split('\n'):
        tree = c.parse(line)
        analysis_results.append(tree.toString(CaboCha.FORMAT_XML))
    return '\n'.join(analysis_results)


def load_dependency_parsing(analytical_data):
    sentence_pattern = r"<sentence>(.+?)</sentence>"
    chunk_pattern = r'<chunk id="(\d*)" link="(.+?)"(.+?)</chunk>'
    morpheme_pattern = r'<tok id="\d*" feature="(.+?),(.+?),' \
                       '(?:.+?),(.+?),(?:.+?)">(.+?)</tok>'
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

    def get_phrase(self):
        show_morphs = []
        for morph in self.morphs:
            if morph.pos != '記号':
                show_morphs.append(morph.surface)
        return ''.join(show_morphs)

    def get_elements(self):
        return f'morphs[{self.get_phrase()}]\t\
dst[{self.dst}]\tsrcs = {self.srcs}'

    def get_pos(self):
        return [morph.pos for morph in self.morphs]

    def get_phrase_n(self):
        show_morphs = []
        for morph in self.morphs:
            if morph.pos != '記号' and morph.pos != '名詞':
                show_morphs.append(morph.surface)
        return ''.join(show_morphs)


def make_received_relates_pass(sentences):
    edges = []
    for chunks in sentences:
        for chunk in chunks:
            phrase = chunk.get_phrase()
            if chunk.dst != -1 and phrase:
                edges.append((chunk, chunks[chunk.dst]))
    chunk_lines = []
    for edge in edges:
        chunk_line = []
        if '名詞' in edge[0].get_pos():
            edge_tuple = edge
            chunk_line.append(edge_tuple[0])
            while True:
                chunk_line.append(edge_tuple[1])
                if edge_tuple[1].dst == -1:
                    break
                edge_tuple = edges[edge_tuple[0].dst]
            chunk_lines.append(chunk_line)

    for n, chunk_line in enumerate(chunk_lines[:-1]):
        for _chunk_line in chunk_lines[n+1:]:
            crosses = list(set(chunk_line) & set(_chunk_line))
            write_line = []
            write_line.append(f'X{chunk_line[0].get_phrase_n()}')
            if len(crosses) == 1:
                write_line.append('|')
                for i, _chunk in enumerate(_chunk_line[:-1]):
                    if i == 0:
                        write_line.append(f'Y{_chunk_line[0].get_phrase_n()}')
                    else:
                        write_line.append(f'-> {_chunk_line[i].get_phrase()}')
                write_line.append(f'| {crosses[0].get_phrase()}')
            else:
                _chunk_line = chunk_line[1:]
                for cross in crosses:
                    _chunk_line.remove(cross)

                for _chunk in _chunk_line:
                    write_line.append(f'-> {_chunk.get_phrase()}')
                write_line.append('-> Y')
            print(' '.join(write_line))

if __name__ == "__main__":
    main()

# これも出来がひどいな...
# 100本終わったら修正するかもしれない
