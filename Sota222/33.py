''' サ変名詞 '''
# サ変接続の名詞をすべて抽出せよ．

import re


def main():
    """main文"""
    file_name = 'neko.txt.mecab'
    contents = read_file(file_name)
    result = load_contents(contents)
    verb_surface = extract_noun_sahen(result)
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


def extract_verb_surface(morphological_list):
    verb_surfaces = []
    for morphological in morphological_list:
        if morphological['pos'] == '動詞':
            verb_surfaces.append(morphological['surface'])
    return verb_surfaces


def extract_verb_base(morphological_list):
    verb_surfaces = []
    for morphological in morphological_list:
        if morphological['pos'] == '動詞':
            verb_surfaces.append(morphological['base'])
    return verb_surfaces


def extract_noun_sahen(morphological_list):
    noun_sahen = []
    for morphological in morphological_list:
        if morphological['pos1'] == 'サ変接続' and morphological['pos'] == '名詞' \
                and not morphological['surface'] == '——':  # 必要か？
            noun_sahen.append(morphological['surface'])
    return noun_sahen

if __name__ == "__main__":
    main()
