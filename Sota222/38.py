''' ヒストグラム '''
# 単語の出現頻度のヒストグラム（横軸に出現頻度，
# 縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．

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
    make_histogram(frequency)


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


def make_histogram(frequency):
    counts = list(zip(*frequency))[1]
    plt.hist(counts, bins=30, range=(1, 30))  # これ以上は種類数が少なく、意味がない
    plt.xlim(xmin=1, xmax=30)
    plt.title('単語の出現頻度のヒストグラム')
    plt.xlabel('単語の出現頻度')
    plt.ylabel('単語の種類数')
    plt.show()


if __name__ == "__main__":
    main()
