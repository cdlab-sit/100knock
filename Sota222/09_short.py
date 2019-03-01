# スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
# それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
# ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
# （例えば"I couldn't believe that I could actually understand
# what I was reading : the phenomenal power of the human mind ."）
# を与え，その実行結果を確認せよ．

import random


def main():
    sentence = "I couldn't believe that I could actually understand what " \
                "I was reading : the phenomenal power of the human mind ."
    list_str = sentence.split(" ")
    shuffle_sentence = " ".join(list(map(shuffle_word, list_str)))
    print(shuffle_sentence)


# 一行にできて笑う
def shuffle_word(word):
    return word[0] + "".join(random.sample([_char for _char in word][1:-1], len(word) - 2)) + word[-1] if not len(word) <= 4 else word


if __name__ == "__main__":
    main()
