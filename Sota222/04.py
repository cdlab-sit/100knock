#"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
import re
string = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
one_letter = [1, 5, 6, 7, 8, 9, 15, 16, 19]
words = re.sub("[,.]", "", string).split(" ")

chemical_symbols = {}

for i, word in enumerate(words):
    chemical_symbols[word[0] if i + 1 in one_letter else word[:2]] = i + 1

print(chemical_symbols)