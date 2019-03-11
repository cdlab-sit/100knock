''' 名詞の連接 '''
# 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ

import re


def main():
    file_name = 'neko.txt.mecab'
    contents = read_file(file_name)
    result = load_contents(contents)
    noun_compound = extract_noun_compound(result)
    print(noun_compound)


def read_file(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()
    return contents


def load_contents(contents):
    morphological_element = ['surface', 'base', 'pos', 'pos1']
    element_place = [0, 7, 1, 2]
    morphological_list = []
    for line in contents.split('\n'):
        if line == 'EOS':
            break
        splited_line = re.split('[\t,]', line)
        morphological = {
            morpho: splited_line[place]
            for morpho, place in zip(morphological_element, element_place)}
        morphological_list.append(morphological)
    return morphological_list


def extract_noun_compound(morphological_list):
    noun_compoundes = []
    nouns = ''
    for morphological in morphological_list:
        if check_morphological(morphological, pos='名詞'):
            nouns += morphological['surface']
        elif nouns:
            noun_compoundes.append(nouns)
            nouns = ''
    return noun_compoundes


def check_morphological(morphological, **elements):
    for e_name, element in elements.items():
        if morphological[e_name] != element:
            return False
    return True

if __name__ == "__main__":
    main()
