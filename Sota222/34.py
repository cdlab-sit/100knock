''' 「AのB」 '''
# 2つの名詞が「の」で連結されている名詞句を抽出せよ．

import re


def main():
    file_name = 'neko.txt.mecab'
    contents = read_file(file_name)
    result = load_contents(contents)
    noun_couples = extract_noun_couple(result)
    print(noun_couples)


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


def extract_noun_couple(morphological_list):
    noun_couples = []
    for i, morphological in enumerate(morphological_list):
        if check_morphological(
                morphological, surface='の', pos='助詞', pos1='連体化') \
                and check_morphological(morphological_list[i - 1], pos='名詞') \
                and check_morphological(morphological_list[i + 1], pos='名詞'):

            noun_couples.append(  # \だと表示の際スペースが空いた
                f"{morphological_list[i - 1]['surface']}" +
                f"{morphological['surface']}" +
                f"{morphological_list[i + 1]['surface']}")

    return noun_couples


def check_morphological(morphological, **elements):
    for e_name, element in elements.items():
        if morphological[e_name] != element:
            return False
    return True

if __name__ == "__main__":
    main()
