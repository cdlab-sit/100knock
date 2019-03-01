# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
#  英小文字ならば(219 - 文字コード)の文字に置換
#  その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．
import string


def cipher(sentence):
    sentence = list(sentence)
    for i, letter in enumerate(sentence):
        alp = string.ascii_lowercase
        if letter in alp:
            sentence[i] = chr(219 - ord(letter))
    return "".join(sentence)

sentence = " Float like a butterfly, die like a bee !!"
print("sentence = \n", sentence)
print("ciphered = \n", cipher(sentence))
