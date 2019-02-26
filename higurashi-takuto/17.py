# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

# Python
col1 = []

with open('hightemp.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    col = line.split('\t')
    col1.append(col[0])

type_string = sorted(set(col1))

print(type_string)

# UNIX
# cut -f 1 -d $'\t' hightemp.txt | sort | uniq
