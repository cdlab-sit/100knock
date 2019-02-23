# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

# Python
with open('hightemp.txt', 'r') as f:
    content = f.read().replace('\t', ' ')

with open('hightemp.txt', 'w') as f:
    f.write(content)

# UNIX
# sed s/$'\t'/' '/g hightemp.txt
