# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

import sys
args = sys.argv

with open("hightemp.txt", "r") as temp_file:
    temp_text = temp_file.readlines()

# 引数がファイルの行数を超えている場合は, ファイルの行数までとする.
# 参照: higurashi-takuto 14.py
row = min(int(args[1]), len(temp_text))

for line in temp_text[:row]:
    print(line.rstrip("\n"))

# UNIX
# head -n 2 hightemp.txt
