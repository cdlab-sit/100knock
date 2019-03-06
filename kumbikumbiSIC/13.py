'''
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．

pasteコマンド
参照：
'''
file_name1 = "col1.txt"
file_name2 = "col2.txt"

merge = []

with open("col1.txt", "r") as col1, open("col2.txt", "r") as col2:
	col1_list = col1.readlines()
	col2_list = col2.readlines()

	for first_col, secound_col in zip(col1_list, col2_list):
		merge.append(first_col.rstrip('\n') + '\t' + secound_col)

with open("merge.txt", "w") as file:
	file.write("".join(merge))

'''
paste col1.txt col2.txt
'''