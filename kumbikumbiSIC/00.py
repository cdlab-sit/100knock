msg = "stressed"

#方法１
print(msg)
print(msg[::-1])

#方法２
#print(type(msg))
msg = list(msg)
#print(type(msg))

for i in range(0, len(msg)):
	print(msg[len(msg) - (i + 1)], end = "")

print("\n")

#参考サイト
#https://qiita.com/okkn/items/54e81346d8f35733ab5e