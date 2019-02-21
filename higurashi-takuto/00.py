# 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

string = 'stressed'

# スライス[開始:終了:ステップ] 開始/終了は省略すると最初から最後まで。ステップはマイナスをつけると最後から
string_backward = string[::-1]

print(string_backward)
