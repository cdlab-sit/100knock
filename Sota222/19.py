'''
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
'''
# python
from os.path import dirname, join
import collections

with open(join(dirname(__file__), 'hightemp.txt'), 'r') as f:
    lines = f.readlines()

pref = []
for line in lines:
    pref.append(line.split()[0])
freq = collections.Counter(pref).most_common()

for line in freq:
    print(line[0])
