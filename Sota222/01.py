#「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．

str = "パタトクカシーー"

#せっかくなんでlambda使ってみました
jump_str = lambda x: x[0::2]

print(jump_str(str))
