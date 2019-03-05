# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

str_p = "パトカー"
str_t = "タクシー"
string = ""

for i in range(4):
    string += str_p[i]
    string += str_t[i]
print(string)

# zip関数を知っていたかった
str_zip = ""
for a, b in zip(str_p, str_t):
    str_zip += a + b
print(str_zip)
