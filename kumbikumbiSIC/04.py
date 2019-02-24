#マップ型の詳細
#https://www.sejuku.net/blog/24759
#高階関数

msg = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
msg2 = msg.split()


##単語ごとにリスト化

# 配列はイテレータブルなのでforで要素を直接取り出せます。
word = []
for w in msg2:
    word.append(w.replace(",", "").replace(".", ""))


# msg2[][]が分かりづらい
chars = []
row = [0,range(4,9),range(14,16),18]

for 

dic = dict(zip(chars,row))
# 辞書型の出力の順番がグチャグチャ
print(dic)
#for char, num in dic.items():
#	print(char + ":" + str(num))
