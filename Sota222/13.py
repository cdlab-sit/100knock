# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目を
# タブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ.

# python

from os.path import dirname, join
f1 = open(join(dirname(__file__), 'col1.txt'), 'r')
f2 = open(join(dirname(__file__), 'col2.txt'), 'r')

f1_lines = f1.readlines()
f2_lines = f2.readlines()
merge = []
for i, line in enumerate(f1_lines):
    merge.append(line.strip('\n') + '\t' + f2_lines[i])

f1.close()
f2.close()

with open(join(dirname(__file__), 'merge.txt'), 'w') as f:
    f.write(''.join(merge))


# UNIX
# paste col1.txt col2.txt > merge.txt
