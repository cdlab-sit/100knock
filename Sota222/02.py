#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ

str1 = "パトカー"
str2 = "タクシー"

str3 = ""
#らっしーさんとほぼ同じになった...
for st1, st2 in zip(str1, str2):
    str3 += st1 + st2

print("str3 = ", str3)
print()
print(str(st1) for st1, st2 in zip(str1, str2))