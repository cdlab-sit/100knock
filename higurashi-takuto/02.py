# 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

string = ['パトカー', 'タクシー']
string_alternate = ''

# なんかもうちょっとオシャレに書けそう。
for a, b in zip(string[0], string[1]):
    string_alternate += a + b

print(string_alternate)
