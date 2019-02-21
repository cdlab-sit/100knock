# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

import re

string = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. '\
         'New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

# 正規表現で,.を消してスペースで分割。
string = re.sub(r'[^\w\s]', '', string)
word = string.split(' ')

# 本当はscope = [0, 4, 5, 6, 7, 8, 14, 15, 18]の一行で18行目までは省略できる。
scope_range = [0, range(4, 9), range(14, 16), 18]
scope = []
for i in scope_range:
    if isinstance(i, int):
        scope.append(i)
    else:
        scope.extend(i)

# 辞書内包表記のif elseはkey, valueそれぞれに必要。
element2num = {_word[:1] if i in scope else _word[:2]: i + 1
               for i, _word in enumerate(word)}

print(element2num)
