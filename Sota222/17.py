# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

# python
import sys
import numpy as np
from pykakasi import kakasi
from os.path import dirname, join
# 漢字を平仮名にするconvを作成
kakasi = kakasi()
kakasi.setMode('J', 'H')  # Japanese(漢字)をasciiに
conv = kakasi.getConverter()

with open(join(dirname(__file__), 'hightemp.txt'), 'r') as f:
    lines = f.readlines()

pref_dict = {}
for line in lines:
    _pref = line.split()[0]
    pref_dict[_pref] = conv.do(_pref)

pref = []
for k, v in sorted(pref_dict.items(), key=lambda x: x[1]):
    pref.append(str(k))

print('\n'.join(pref))

# UNIX
# cut -f 1 -d $' ' hightemp.txt | sort | uniq
