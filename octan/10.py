# 行数をカウントせよ．確認にはwcコマンドを用いよ．

with open("hightemp.txt", "r") as temp_file:
    num_of_lines = len(temp_file.readlines())
    # num_of_lines = sum(1 for line in open("hightemp.txt", "r"))  #別解
    print(num_of_lines)

# UNIXコマンド
# wc -l hightemp.txt
