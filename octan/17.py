# 1列目の文字列の種類（異なる文字列の集合）を求めよ．
# 確認にはsort, uniqコマンドを用いよ．

col1_list = []

with open("hightemp.txt", "r") as temp_file:
    lines = temp_file.readlines()

for line in lines:
    line_list = line.split()
    col1_list.append(line_list[0])

prefec_list = list(set(col1_list))
print(prefec_list)

# UNIX
# cut -f 1 -d $' ' hightemp.txt | sort | uniq
