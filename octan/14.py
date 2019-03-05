# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

import sys
args = sys.argv

with open("hightemp.txt", "r") as temp_file:
    lines = temp_file.readlines()

for row in range(int(args[1])):
	line = lines[row].rstrip("\n")
    print(line)
