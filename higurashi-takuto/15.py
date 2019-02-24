# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．

# Python
import argparse

# コマンドライン引数の設定
parser = argparse.ArgumentParser(description='tail')
parser.add_argument('--lines', '-n', type=int, default=10, help='表示行数')
args = parser.parse_args()

with open('hightemp.txt', 'r') as f:
    lines = f.readlines()

# ファイル行数を超えてる場合はファイル行数までにする。
n = min(args.lines, len(lines))
for line in lines[len(lines)-n:]:
    print(line, end='')

# UNIX
# tail -n 5 hightemp.txt
