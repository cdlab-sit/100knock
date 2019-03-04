# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

# python
import sys
from os.path import dirname, join

args = sys.argv
N = args[1]
with open(join(dirname(__file__), 'hightemp.txt'), 'r') as f:
    lines = f.readlines()
for i in range(int(N)):
    print(lines[i], end='')

# UNIX
# head -n 3 hightemp.txt
