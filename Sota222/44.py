''' 係り受け木の可視化 '''
# 与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，
# Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
import re
import CaboCha
import pydot_ng as pdt


def main():
    input_line = input('グラフにしたい文を入力してください\n:')
    input_line_cabocha = dependency_parsing(input_line)
    sentence_list = load_dependency_parsing(input_line_cabocha)
    write_directed_graph(sentence_list)


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


def write_directed_graph(sentences):
    edges = []
    for chunks in sentences:
        for chunk in chunks:
            phrase = chunk.get_phrase()
            if chunk.dst != -1 and phrase:
                print((f'{phrase}\t{chunks[chunk.dst].get_phrase()}\n'))
                edges.append((phrase, chunks[chunk.dst].get_phrase()))
    # g = pdt.graph_from_edges(edges)
    g = pdt.graph_from_edges(edges, directed=True)
    g.write_jpeg('graph_from_edges_dot.jpg', prog='dot')

if __name__ == "__main__":
    main()
