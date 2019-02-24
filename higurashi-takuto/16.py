# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

# Python
import math
import argparse

# コマンドライン引数の設定
parser = argparse.ArgumentParser(description='head')
parser.add_argument('--lines', '-n', type=int, default=10, help='表示行数')
args = parser.parse_args()

with open('hightemp.txt', 'r') as f:
    lines = f.readlines()

# ファイル行数を超えてる場合はファイル行数までにする。
n = min(args.lines, len(lines))
num_file = math.ceil(len(lines) / n) if n != 0 else 0
# スライスとか使って2重ループじゃなくもできそう。
for i in range(num_file):
    content = []
    for line in lines[i*n:(i+1)*n]:
        content.append(line)
    with open(f'hightemp_{i+1}', 'w') as f:
        f.write(''.join(content))

# UNIX
# split -l 5 hightemp.txt hightemp_
