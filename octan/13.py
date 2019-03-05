# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
# 確認にはpasteコマンドを用いよ．

with open("col1.txt", "r") as col1_file:
    col1_list = col1_file.readlines()

with open("col2.txt", "r") as col2_file:
    col2_list = col2_file.readlines()

marge_list = []
for col1_word, col2_word in zip(col1_list, col2_list):
    marge_list.append(col1_word.rstrip("\n") + "\t" + col2_word)

marge_text = "".join(marge_list)
with open("marge_col.txt", "w") as marge_file:
    marge_file.write(marge_text)

# UNIXコマンド
# paste col1.txt col2.txt > marge_col.txt
