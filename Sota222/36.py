''' 単語の出現頻度 '''
# 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

import re
import collections


def main():
    file_name = 'neko.txt.mecab'
    contents = read_file(file_name)
    result = load_contents(contents)
    frequency = get_frequency(result)
    for word in frequency:
        print(f'単語:{word[0]}, 出現頻度:{word[1]}')
        if int(word[1]) < 100:  # すべて表示するとわかりづらいので途中まで
            break


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


def get_frequency(morphological_list):
    words = []
    for morphological in morphological_list:
        words.append(morphological['surface'])
    freq = collections.Counter(words).most_common()
    return freq


if __name__ == "__main__":
    main()
