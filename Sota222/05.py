# 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
# この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．


def n_gram(string, n):
    return [string[i: i + n] for i in range(len(string) - n + 1)]

string = 'I am an NLPer'
word = string.split(' ')

word_bi_gram = n_gram(word, 2)
char_bi_gram = n_gram(string, 2)

print(word_bi_gram)
print(char_bi_gram)
