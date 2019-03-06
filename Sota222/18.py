'''
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
'''
# python
from os.path import dirname, join
from operator import itemgetter

with open(join(dirname(__file__), 'hightemp.txt'), 'r') as f:
    lines = f.readlines()

hightemp = []
for line in lines:
    hightemp.append(line.split())

hightemp.sort(key=itemgetter(2))

hightemp = '\n'.join(map(' '.join, hightemp))

with open(join(dirname(__file__), 'sort.txt'), 'w') as f:
    f.write(hightemp)

# UNIX
# sort -k 3 -t " " hightemp.txt
