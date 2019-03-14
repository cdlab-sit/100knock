''' 係り受け解析結果の読み込み（形態素） '''
# 40に加えて，文節を表すクラスChunkを実装せよ．
# このクラスは形態素（Morphオブジェクト）のリスト（morphs），係り先文節インデックス番号（dst），
# 係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
# さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，
# 8文目の文節の文字列と係り先を表示せよ．第5章の残りの問題では，ここで作ったプログラムを活用せよ．

import re


def main():
    file_name = 'neko.txt.cabocha'
    neko_txt_cabocha = read_file(file_name)
    result_dependency_parsing = load_dependency_parsing(neko_txt_cabocha)
 
    for a in result_dependency_parsing[7]:
        print(a.show_elements())

def read_file(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()
    return contents


def load_dependency_parsing(analytical_data):
    sentence_pattern = r"<sentence>(.+?)</sentence>"
    chunk_pattern = r'<chunk id="\d*" link="(.+?)"(.+?)</chunk>'
    morpheme_pattern = r'<tok id="\d*" feature="(.+?),(.+?),' \
                       '(?:.+?),(.+?),(?:.+?)">(.+?)</tok>'
    sentences = re.findall(sentence_pattern, analytical_data, flags=re.DOTALL)
    sentence_list = []
    for sentence in sentences:
        chunks = re.findall(chunk_pattern, sentence, flags=re.DOTALL)
        chunk_class_list = []
        for chunk in chunks:
            morphemes = re.findall(morpheme_pattern, chunk[1], flags=re.DOTALL)
            morph_class_list = []
            for morpheme in morphemes:
                m = Morph(morpheme[3], morpheme[2], morpheme[0], morpheme[1])
                morph_class_list.append(m)
            c = Chunk(morph_class_list, chunk[0], '?') # あとで変更
            chunk_class_list.append(c)
        sentence_list.append(chunk_class_list)
    return sentence_list


class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def show_elements(self):
        return f'surface = {self.surface}\tbase = {self.base}\t\
pos = {self.pos}\tpos1 = {self.pos1}'


class Chunk():
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def show_elements(self):
        return f'<{self.morphs[0].show_elements()}>\tdst = {self.dst}\t\
srcs = {self.srcs}'  # どーしよーかなー

if __name__ == "__main__":
    main()
