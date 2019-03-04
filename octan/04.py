# "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
# という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
# 取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might"\
    " Also Sign Peace Security Clause. Arthur King Can."
str.replace(".", "")
word_list = str.split()
two_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
elment_dic = {}

for i in range(len(word_list)):
    if i + 1 in two_list:
        elment_dic[word_list[i][0]] = i + 1
    else:
        elment_dic[word_list[i][0:2]] = i + 1
print(elment_dic)

# enumerate()使用
elment_dic = {}
for i, word in enumerate(word_list, 1):
    if i in two_list:
        elment_dic[word[0]] = i
    else:
        elment_dic[word[0:2]] = i
print(elment_dic)
