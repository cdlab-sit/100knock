# 行数をカウントせよ．確認にはwcコマンドを用いよ．

# Python
from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, "./hightemp.txt")
f = open(file_path, 'r')
print(len(f.readlines()))
f.close

# UNIX
# wc -l hightemp.txt
