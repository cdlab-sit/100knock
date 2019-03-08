# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．
# 同様の処理をsplitコマンドで実現せよ．

import argparse

parser = argparse.ArgumentParser(description='引数分の行数で分割する(split)')
parser.add_argument(
    'range_slice', type=int, default=3,
    help='int型(自然数)'
)
args = parser.parse_args()

with open('hightemp.txt', 'r') as temp_file:
    temp_text = temp_file.readlines()
n_lines = len(temp_text)

# 引数がファイルの行数を超えている場合は, ファイルの行数までとする.
# 参照: higurashi-takuto 14.py
range_slice = min(args.range_slice, n_lines)

for start in range(0, n_lines, range_slice):
    # 0からテキストの行数分まで、引数分だけステップするrange()のリストを作る
    slice_text = ''.join(temp_text[start:start + range_slice])
    with open(f'{"slice_temp_"}{start / range_slice}', 'w') as slice_file:
        slice_file.write(slice_text)

# UNIX
# split -l 3 hightemp.txt slice_temp_
