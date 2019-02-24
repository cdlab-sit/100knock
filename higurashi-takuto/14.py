# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．

# Python
import argparse

# コマンドライン引数の設定
parser = argparse.ArgumentParser(description='head')
parser.add_argument('--lines', '-n', type=int, default=10, help='表示行数')
args = parser.parse_args()

with open('hightemp.txt', 'r') as f:
    lines = f.readlines()

# ファイル行数を超えてる場合はファイル行数までにする。
for i in range(min(args.lines, len(lines))):
    print(lines[i], end='')

# UNIX
# head -n 5 hightemp.txt
