# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，
# もしくはexpandコマンドを用いよ．

# python
from os.path import dirname, join
current_dir = dirname(__file__)
file_path = join(current_dir, './hightemp.txt')

with open(file_path, 'r') as f:
    _line = f.read().replace('\t', ' ')
    print(_line)

with open(file_path, 'w') as f:
    f.write(_line)

# UNIX
# cat hightemp.txt | tr '\t' ' '
