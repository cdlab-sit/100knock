# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．


def n_gram(str, n):
    ngr_list = []

    for i in range(len(str) - n + 1):
        ngr_list.append(str[i:i + n])

    return ngr_list

str = "I am an NLPer"
word_list = str.split()

print(n_gram(word_list, 2))  # 単語グラム
print(n_gram(str, 2))  # 文字グラム
