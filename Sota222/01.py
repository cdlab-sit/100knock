#「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

str1 = "パタトクカシーー"
str2 = "Frleamnidlriea"
#せっかくなんでlambda使ってみました
jump_str = lambda x: x[0::2]

print(jump_str(str1))
print()
print(jump_str(str2))