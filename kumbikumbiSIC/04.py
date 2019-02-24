#マップ型の詳細
#https://www.sejuku.net/blog/24759
#高階関数

msg = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
msg2 = msg.split()


##単語ごとにリスト化

# 配列はイテレータブルなのでforで要素を直接取り出せます。
words = []
for w in msg2:
    words.append(w.replace(",", "").replace(".", ""))

#参考：https://qiita.com/segavvy/items/4e592dea2f828e5385ff
chars = {}
one_char = [0,5,6,7,8,9,15,16,18]

for num,word in enumerate(words,1):
	if num in one_char:
		chars[word[0:1]] = num
	else:
		chars[word[0:2]] = num

print(chars)