''' 頻度上位10語 '''
# 出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

import re
import collections
import matplotlib.pyplot as plt
import random


def main():
    file_name = 'neko.txt.mecab'
    contents = read_file(file_name)
    result = load_contents(contents)
    frequency = get_frequency(result)
    make_bar_graph(frequency, 10)


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


def make_bar_graph(frequency, count):
    x = []
    y = []
    for i, word in enumerate(frequency):
        x.append(word[0])
        y.append(word[1])
        if i > 10:
            break
    plt.bar(x, y, tick_label=y)
    plt.show()
    print(x)
    print(y)

if __name__ == "__main__":
    main()
