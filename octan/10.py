# 行数をカウントせよ．確認にはwcコマンドを用いよ．

temp_file = open("hightemp.txt", "r")
print(len(temp_file.readlines()))
# print(sum(1 for line in open("hightemp.txt", "r")))  #別解
temp_file.close()
