#マップ型の詳細
#https://www.sejuku.net/blog/24759
#高階関数

msg = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
msg2 = msg.split()
msg3 = msg.split()


##単語ごとにリスト化

# 方法1: 配列はイテレータブルなのでforで要素を直接取り出せます。
word = []
for w in msg2:
    word.append(w.replace(",", "").replace(".", ""))
#print("word:", word)

# 方法2: インデックスをつけたい場合はenumerate()が使えます。
for i, w in enumerate(msg2):
    msg2[i] = w.replace(",", "").replace(".", "")
#print("msg2:", msg2)

# 方法3: また、配列の全要素に同じ処理をするにはmap()が使えます。（戻り値がmapなのでlistにする必要があります）
msg3 = list(map(lambda word: word.replace(",", "").replace(".", ""), msg3))
#print("msg3:", msg3)

##上記の方法３つの出力が同じになる事を確認


# 頭が悪いけど、これしか思いつかなかった
# スマートさに欠けている
# msg2[][]が分かりづらい
chars = []
row = []

for i,w in enumerate(msg2):
	if(i==0 or i==18 or i==14 or i==15):
		chars.append(msg2[i][0])
	else:
		chars.append(msg2[i][0] + msg2[i][1])
	#print(chars[i])
	row.append(i+1)
	#print(row[i])

for i,w in enumerate(msg2[4:10]):
	print(chars[i+4])
	chars[i+4] = msg2[i+4][0]
	print(chars[i+4])

dic = dict(zip(chars,row))
# 辞書型の出力の順番がグチャグチャ
print(dic)
#for char, num in dic.items():
#	print(char + ":" + str(num))
