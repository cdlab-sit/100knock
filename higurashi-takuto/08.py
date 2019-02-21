# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．


def cipher(string):
    return ''.join([chr(219-ord(char)) if char.islower() else char
                    for char in string])


# 2回通すと復元される。入力の文字コードをnとすると
#  入力: n
# 1回目: 219 - n
# 2回目: 219 - (219 - n) = n
string = input()
ciphered = cipher(string)
decrypted = cipher(ciphered)

print(string, ciphered, decrypted)
