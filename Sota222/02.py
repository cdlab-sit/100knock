#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ

str1 = "パトカー"
str2 = "タクシー"

plus_str = lambda x, y: x + y
print(''.join([plus_str(st1, st2) for st1, st2 in zip(str1, str2)]))
