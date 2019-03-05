# 11. タブをスペースに置換タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

with open("hightemp.txt", "r") as temp_file:
    temp_file_text = temp_file.read()
    space_temp_file_text = temp_file_text.replace("\t", " ")

with open("space_hightemp.txt", "w") as space_temp_file:
    space_temp_file.write(space_temp_file_text)

# UNIXコマンド
# tr '\t' ' ' < hightemp.txt
