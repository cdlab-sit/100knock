# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

str_p = "パトカー"
str_t = "タクシー"
str = ""

for i in range(4):
    str += str_p[i]
    str += str_t[i]
print(str)

# zip関数を知っていたかった
str_zip = ""
for a, b in zip(str_p, str_t):
    str_zip += a + b
print(str_zip)
