'''
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはsort, uniqコマンドを用いよ．

set 参照
https://note.nkmk.me/python-set/

UNIX 参照：higurashi-takuto
cut -f 1 -d $'\t' hightemp.txt | sort | uniq
'''

with open("hightemp.txt", "r") as f:
	lines = f.readlines()

words = set()
for line in lines:
		cols = line.split('\t')
		words.add(cols[0])

for word in sorted(words):
	print(word)