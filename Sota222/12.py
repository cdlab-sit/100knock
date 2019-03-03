# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとして
# ファイルに保存せよ．確認にはcutコマンドを用いよ．

# python
from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, './hightemp.txt')

# lines = None　いらなかった！！！
with open(file_path, 'r') as f:
    lines = f.readlines()

prefecture = []
region = []
for line in lines:
    line = line.split()  # 引数なしで スペース、タブ、改行で分割
    prefecture.append(line[0])
    region.append(line[1])

file_path = join(current_dir, 'col1.txt')
with open(file_path, 'w') as f:
    f.write(str(prefecture))
file_path = join(current_dir, 'col2.txt')
with open(file_path, 'w') as f:
    f.write(str(region))


print(prefecture)

# UNIX
# cat hightemp.txt | tr '\t' ' '
