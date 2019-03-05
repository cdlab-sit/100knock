# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

col1_list = []
col2_list = []

with open("hightemp.txt", "r") as temp_file:
    lines = temp_file.readlines()

for line in lines:
    line_list = line.split()
    col1_list.append(line_list[0])
    col2_list.append(line_list[1])

col1_text = "\n".join(col1_list)
col2_text = "\n".join(col2_list)

with open("col1.txt", "w") as col1_file:
    col1_file.write(col1_text)

with open("col2.txt", "w") as col2_file:
    col2_file.write(col2_text)

# UNIXコマンド
# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt
