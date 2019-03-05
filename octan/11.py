# 11. タブをスペースに置換タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

temp_file = open("hightemp.txt", "r")
new_temp_file = open("space_hightemp.txt", "w")
temp_text = temp_file.read()
new_temp_file.write(temp_text.replace("\t", " "))

'''
# 別解?
for line in temp_file:
    line = line.replace("\t", " ")
    new_temp_file.write(line)
'''

temp_file.close()
new_temp_file.close()
