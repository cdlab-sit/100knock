# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ

# 初期
str = "パタトクカシーー"
str_slice = str[0:1] + str[2:3] + str[4:5] + str[6:7]
print(str_slice)

# ステップなんて知らなかったんです
str_step = str[::2]
print(str_step)

# 初期案ならスライス使う必要ないよね常識的に考えて
str_slice2 = "パタトクカシーー"
str_slice2 = str[0] + str[2] + str[4] + str[6]
print(str_slice)
