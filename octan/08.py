# 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# *英小文字ならば(219 - 文字コード)の文字に置換
# *その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ．


def cipher(line):
    ci_line = ""
    for char in line:
        if ord("a") <= ord(char) <= ord("z"):
            char = chr(219 - ord(char))
        ci_line += char
    return ci_line

string = "abCdeFいろは"
print("変化前: ", string)
string = cipher(string)
print("暗号化: ", string)
string = cipher(string)
print("復号化: ", string)
