'''
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ

UNIX
tail -n 5 hightemp.txt
'''
import sys

# コマンドライン引数の設定
args = sys.argv
n = int(args[1])

with open("hightemp.txt", "r") as f:
	lines = f.readlines()

	# ファイル行数を超えてる場合はファイル行数までにする
	n = min(len(lines), n)

	for line in lines[-n::]:
		print(line, end="")