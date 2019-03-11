''' 動詞の原形 '''
# 動詞の原形をすべて抽出せよ．

import re


def main():
    file_name = 'neko.txt.mecab'
    contents = read_file(file_name)
    result = load_contents(contents)
    verb_surface = extract_verb_base(result)
    print(verb_surface)


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


def extract_verb_base(morphological_list):
    verb_bases = []
    for morphological in morphological_list:
        if morphological['pos'] == '動詞':
            verb_bases.append(morphological['base'])
    return verb_bases

if __name__ == "__main__":
    main()
