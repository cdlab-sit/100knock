'''
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ

sys.argv 参照
https://qiita.com/orange_u/items/3f0fb6044fd5ee2c3a37

argparse 参照
https://docs.python.org/ja/3/library/argparse.html

head 参照
https://eng-entrance.com/linux-command-head


解答コマンド
head -n 4 hightemp.txt

'''

import sys

# コマンドライン引数の設定
# File_Name n  で実行
args = sys.argv
n = int(args[1])

with open("hightemp.txt", "r") as f:
	lines = f.readlines()
	for row in range(n):
		print(lines[row].rstrip("\n"))

