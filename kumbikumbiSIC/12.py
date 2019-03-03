'''
1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

参考　12.pyの答え　	：　https://qiita.com/segavvy/items/51a515c19bcd29b13b7f
参考　open()について	：　https://note.nkmk.me/python-file-io-open-with/
参考　明示的な改行		：　https://www.glamenv-septzen.net/view/185
参考　ジェネレータについて(先頭の関数について)	:	https://qiita.com/tomotaka_ito/items/15b5999c76001dbc9a58
										:	https://qiita.com/tomotaka_ito/items/35f3eb108f587022fa09
'''

file_name = "hightemp.txt"

with open(file_name) as file, open("col1.txt", "w") as col1, \
	open("col2.txt", "w") as col2:

	lines = file.readlines();

	for line in lines:
		cols = line.split("\t")
		col1.write(cols[0] + "\n")
		col2.write(cols[1] + "\n")


'''
cut 参考url
http://x68000.q-e-d.net/~68user/unix/pickup?cut


'''