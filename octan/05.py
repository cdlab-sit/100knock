# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．


def n_gram(string, n):
    ngram_list = []

    for count in range(len(string) - n + 1):
        ngram_list.append(string[count:count + n])

    return ngram_list

string = "I am an NLPer"
word_list = string.split()

word_2_gram = n_gram(word_list, 2)  # 単語グラム
print(word_2_gram)
char_2_gram = n_gram(word_list, 2)  # 文字グラム
print(char_2_gram)
