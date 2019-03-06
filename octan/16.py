# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

import argparse

parser = argparse.ArgumentParser(description='引数分の行数で分割する(split)')
parser.add_argument(
    'n_line', type=int, default=3,
    help='int型(自然数)'
)
args = parser.parse_args()

with open('hightemp.txt', 'r') as temp_file:
    temp_text = temp_file.readlines()
len_text = len(temp_text)

# 引数がファイルの行数を超えている場合は, ファイルの行数までとする.
# 参照: higurashi-takuto 14.py
n_line = min(args.n_line, len_text)

for start in range(0, len_text, n_line):
    # 0からテキストの行数分まで、引数分だけステップするrange()のリストを作る
    slice_text = ''.join(temp_text[start:start + n_line])
    with open(f'{"slice_temp_"}{start / n_line}', 'w') as slice_file:
        slice_file.write(slice_text)

# UNIX
# split -l 3 hightemp.txt slice_temp_
