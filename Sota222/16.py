# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

# python
import sys
import numpy as np
from os.path import dirname, join

args = sys.argv
N = int(args[1])

with open(join(dirname(__file__), 'hightemp.txt'), 'r') as f:
    lines = f.readlines()

split_sheets = list(np.array_split(lines, N))

for i, sheet in enumerate(split_sheets):
    with open(
        join(dirname(__file__), 'split_sheet_{}.txt'.format(i)), 'w'
    ) as f:
        f.write(''.join(sheet))

# UNIX
# split -l 3 hightemp.txt split_txt
