# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．
# 確認にはtailコマンドを用いよ．

import argparse

parser = argparse.ArgumentParser(description='末尾から引数分の行数表示する(tail)')
parser.add_argument(
    'n_line', type=int, default=1,
    help='int型(負の数でも動作可能だが、tailコマンドの代用と考えると自然数が好ましい)'
)
args = parser.parse_args()

with open('hightemp.txt', 'r') as temp_file:
    temp_text = temp_file.readlines()

# 引数がファイルの行数を超えている場合は, ファイルの行数までとする.
# 参照: higurashi-takuto 14.py
n_line = min(args.n_line, len(temp_text))

for line in temp_text[-n_line:]:
    print(line.rstrip('\n'))

# UNIX
# tail -n 2 hightemp.txt
