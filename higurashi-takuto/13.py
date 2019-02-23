# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

# Python
col1 = []
col2 = []

with open('col1.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        col1.append(line.rstrip('\r\n'))

with open('col2.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        col2.append(line.rstrip('\r\n'))

with open('col1_2.txt', 'w') as f:
    f.write('\n'.join([f'{_col1}\t{_col2}'
                       for _col1, _col2 in zip(col1, col2)]))

# UNIX
# paste col1.txt col2.txt > col1_2.txt
