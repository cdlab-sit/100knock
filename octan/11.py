# 11. タブをスペースに置換タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

temp_file = open("hightemp.txt", "r")
space_temp_file = open("space_hightemp.txt", "w")
temp_file_text = temp_file.read()
space_temp_file_text = temp_file_text.replace("\t", " ")
space_temp_file.write(space_temp_file_text)

'''
# 別解?
for line in temp_file:
    line = line.replace("\t", " ")
    space_temp_file.write(line)
'''

temp_file.close()
space_temp_file.close()

# UNIXコマンド
# tr '\t' ' ' < hightemp.txt
