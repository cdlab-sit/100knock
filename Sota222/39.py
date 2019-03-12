''' Zipfの法則 '''
# 単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

import re
import collections
import matplotlib.pyplot as plt

font = {"family": "IPAexGothic"}  # フォントを変更
plt.rc('font', **font)  # フォントを変更


def main():
    file_name = 'neko.txt.mecab'
    contents = read_file(file_name)
    result = load_contents(contents)
    frequency = get_frequency(result)
    make_double_log_graph(frequency)


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


def make_double_log_graph(frequency):
    counts = list(zip(*frequency))[1]
    plt.scatter(range(1, len(counts) + 1), counts)
    plt.xscale('log')
    plt.yscale('log')
    plt.grid(axis='both')
    plt.title('両対数グラフ')
    plt.xlabel('単語の出現頻度順位')
    plt.ylabel('出現頻度')
    plt.show()


if __name__ == "__main__":
    main()
