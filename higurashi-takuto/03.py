# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．

import re

string = 'Now I need a drink, alcoholic of course, '\
         'after the heavy lectures involving quantum mechanics.'
# 正規表現で,.を消してスペースで分割、その後文字列の長さを見る。
string = re.sub(r'[^\w\s]', '', string)
num_char = list(map(len, string.split(' ')))

print(num_char)
