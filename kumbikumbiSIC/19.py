'''
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ

UNIX
cut -f 1 -d $'\t' hightemp.txt | sort | uniq -c | sort -r
'''
with open("hightemp.txt", "r") as f:
	lines = f.readlines()

# coloum1 作成
col1 = []
for line in lines:
	col1.append(line.split("\t")[0])

# the 力技
col1.sort()

# 連続で続く文字列をカウント（ソートされている）
ans = []
ans_col = []

pre_word = col1[0]
word_c = 0

for index, word in enumerate(col1):
	if word == pre_word:
		word_c = word_c+1
	else:
		#print(f"{pre_word}: {word_c}")
		ans_col.append(word_c)
		ans_col.append(pre_word)
		ans.append(ans_col)

		#初期化
		word_c = 1
		pre_word = word
		ans_col = []

# 自分用メモ：よく分からん
#https://qiita.com/segavvy/items/adee520db1a257e347d5
ans.sort(key=lambda line: int(line[0]), reverse=True)
for line in ans:
	# UNIXに出力を合わせた
	print(f'   {line[0]} {line[1]}')