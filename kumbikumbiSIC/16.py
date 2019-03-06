'''
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．

UNIX
split -l 4 hightemp.txt hightemp16_
'''
import sys

# コマンドライン引数の設定
args = sys.argv
n = int(args[1])

with open("hightemp.txt", "r") as f:
	lines = f.readlines()

if n > len(lines) or n == 0:
	print("入力エラー")
else :
	lines_file = []
	for i in range(0,len(lines),n):	
		lines_file.append(lines[i:i+n])
		with open(f"hightemp16_{int(i/n+1)}.txt", "w") as f:
			f.write("".join(lines_file[int(i/n)]))