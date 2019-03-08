# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
# 確認にはcut, uniq, sortコマンドを用いよ．

from operator import itemgetter

with open("hightemp.txt", "r") as temp_file:
    lines = temp_file.readlines()

col1_list = []
for line in lines:
    line_list = line.split()
    col1_list.append(line_list[0])

prefec_list = list(set(col1_list))
freq_list = []
for prefec in prefec_list:
    freq_list.append([prefec, col1_list.count(prefec)])

freq_list.sort(key=itemgetter(1))  # 各リストの2番目の要素をキーに
for list_line in freq_list[::-1]:
    print(list_line[0], ':出現 ', list_line[1], '回')

# UNIX
# 
