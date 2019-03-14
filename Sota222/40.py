''' 係り受け解析結果の読み込み（形態素） '''
# 形態素を表すクラスMorphを実装せよ．
# このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
# メンバ変数に持つこととする．さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
# 各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．

import re


def main():
    file_name = 'neko.txt.cabocha'
    neko_txt_cabocha = read_file(file_name)
    result = load_dependency_parsing(neko_txt_cabocha)
    sentence = int(input('何文目の形態素列を表示させますか？'))
    for morph in result[sentence - 1]:
        print(morph.show_elements())


def read_file(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()
    return contents


def load_dependency_parsing(analytical_data):
    sentence_pattern = r"<sentence>(.+?)</sentence>"
    morpheme_pattern = r'<tok id="\d*" feature="(.+?),(.+?),(?:.+?),(?:.+?)' \
                       ',(?:.+?),(?:.+?),(.+?),(?:.+?)">(.+?)</tok>'
    sentences = re.findall(sentence_pattern, analytical_data, flags=re.DOTALL)
    sentences_list = []
    for sentence in sentences:
        morphemes = re.findall(morpheme_pattern, sentence, flags=re.DOTALL)
        morph_class_list = []
        for morpheme in morphemes:
            m = Morph(morpheme[3], morpheme[2], morpheme[0], morpheme[1])
            morph_class_list.append(m)
        sentences_list.append(morph_class_list)
    return sentences_list


class Morph():

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def show_elements(self):
        return f'surface = {self.surface}\tbase = {self.base}\t\
pos = {self.pos}\tpos1 = {self.pos1}'


if __name__ == "__main__":
    main()
