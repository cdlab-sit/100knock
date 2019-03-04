# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

# python
import sys
from os.path import dirname, join

args = sys.argv
N = args[1]
with open(join(dirname(__file__), 'hightemp.txt'), 'r') as f:
    lines = f.readlines()
for i in range(int(N)):
    print(lines[len(lines) - int(N) + i], end='')

# UNIX
# tail -n 3 hightemp.txt
