# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# Python
with open('hightemp.txt', 'r') as f:
    # readline()は1行ずつ読むので、全部の行を読むにはreadlines()
    print(len(f.readlines()))

# UNIX
# wc -l hightemp.txt
