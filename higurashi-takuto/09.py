# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，その実行結果を確認せよ．

import random


def typoglycemia(word):
    if len(word) > 4:
        word_middle = list(word[1:-1])
        random.shuffle(word_middle)
        word = word[0] + ''.join(word_middle) + word[-1]
    return word


string = 'I couldn\'t believe that I could actually understand '\
         'what I was reading : the phenomenal power of '\
         'the human mind .'

string_typoglycemia = ' '.join(map(typoglycemia, string.split(' ')))

print(string_typoglycemia)
