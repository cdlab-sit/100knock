# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

# python
import sys
import numpy as np
from os.path import dirname, join

with open(join(dirname(__file__), 'hightemp.txt'), 'r') as f:
    lines = f.readlines()

prefecture = []
for line in lines:
    prefecture.append(line.split()[0])

prefecture = sorted(set(prefecture))
print(prefecture)

# UNIX
# cut -f 1 -d $' ' hightemp.txt | sort | uniq
