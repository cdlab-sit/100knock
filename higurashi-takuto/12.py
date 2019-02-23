# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

# Python
col1 = []
col2 = []

with open('hightemp.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    col = line.split('\t')
    col1.append(col[0])
    col2.append(col[1])

with open('col1.txt', 'w') as f:
    f.write('\n'.join(col1))

with open('col2.txt', 'w') as f:
    f.write('\n'.join(col2))

# UNIX
# cut -f 1 -d $'\t' hightemp.txt > col1.txt
# cut -f 2 -d $'\t' hightemp.txt > col2.txt
