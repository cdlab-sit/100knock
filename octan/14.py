# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．
# 確認にはheadコマンドを用いよ．

import argparse
parser = argparse.ArgumentParser(description='引数分の行数表示する(head)')
parser.add_argument(
    'n_line', type=int, default=0.01,
    help='int型(マイナスでも動作可能だが、headコマンドの代用と考えると自然数が好ましい)'
)
args = parser.parse_args()

with open('hightemp.txt', 'r') as temp_file:
    temp_text = temp_file.readlines()

# 引数がファイルの行数を超えている場合は, ファイルの行数までとする.
# 参照: higurashi-takuto 14.py
n_line = min(args.n_line, len(temp_text))

for line in temp_text[:n_line]:
    print(line.rstrip('\n'))

# UNIX
# head -n 2 hightemp.txt
