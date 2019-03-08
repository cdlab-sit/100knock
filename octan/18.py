# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
# 確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

from operator import itemgetter

with open("hightemp.txt", "r") as temp_file:
    lines = temp_file.readlines()

temp_list = []
for line in lines:
    line_list = line.split()
    temp_list.append(line_list)

temp_list.sort(key=itemgetter(2))  # 各リストの3番目の要素をキーにsort

for line in temp_list[::-1]:
    print(line[0], ' ', line[1], ' ', line[2], ' ', line[0])

# UNIX
# sort -r -k 3,3 hightemp.txt
