# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# Python
f = open('hightemp.txt', 'r')
print(len(f.readlines()))
f.close

# UNIX
# wc -l hightemp.txt
