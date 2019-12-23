# -*- coding: utf-8 -*-
# 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ

# 初期
string = "パタトクカシーー"
str_slice = string[0:1] + string[2:3] + string[4:5] + string[6:7]
print(str_slice)

# ステップなんて知らなかったんです
str_step = string[::2]
print(str_step)

# 初期案ならスライス使う必要ないよね常識的に考えて
str_slice2 = "パタトクカシーー"
str_slice2 = string[0] + string[2] + string[4] + string[6]
print(str_slice2)
