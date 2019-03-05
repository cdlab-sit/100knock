# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
# 確認にはcutコマンドを用いよ．

temp_file = open("hightemp.txt", "r")
col_file_1 = open("col1.txt", "w")
col_file_2 = open("col2.txt", "w")

for line in temp_file:
    line_list = line.split()
    col_file_1.write(line_list[0] + "\n")
    col_file_2.write(line_list[1] + "\n")

temp_file.close()
col_file_1.close()
col_file_2.close()

# UNIXコマンド
# cut -f 1 hightemp.txt > col1.txt
# cut -f 2 hightemp.txt > col2.txt
