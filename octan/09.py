# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．
# 適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．
import random


def typoglycemia(string):
    words_list = string.split()
    typo_words_list = []
    for word in words_list:
        if 4 < len(word):
            word = word[0] + \
                "".join(random.sample(word[1:-1], len(word[1:-1]))) + word[-1]
        typo_words_list.append(word)
    return " ".join(typo_words_list)

string = "I couldn't believe that I could actually understand what I was"\
    " reading : the phenomenal power of the human mind ."
typo_string = typoglycemia(string)
print(typo_string)
