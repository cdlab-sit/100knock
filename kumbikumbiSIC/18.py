'''
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

reverse 参照
https://note.nkmk.me/python-reverse-reversed/

UNIX
sort -k 3 -r hightemp.txt
'''

with open("hightemp.txt", "r") as f:
	lines = f.readlines()

	# reverseは文字列、タプルには使用不可能（更新不可能だから）
	# ただ、３コラムに数値がなければ使用できないので応用性はない
	lines.reverse()

	for line in lines[::-1]:
		print(line, end="")