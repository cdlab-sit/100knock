# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，
# もしくはexpandコマンドを用いよ．
from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./hightemp.txt")

with open(file_path, 'r') as f:
    _line = f.read().replace('\t', ' ')
    print(_line)
