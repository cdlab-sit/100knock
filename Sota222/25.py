''' テンプレートの抽出 '''
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
# 辞書オブジェクトとして格納せよ．
import re
import json
file_name = 'article_UK.json'

with open(file_name, "r") as f:
    article_UK = json.load(f)

basic_pattern = r'\|(.+?) = (.+?)\n'
basic_info = re.findall(basic_pattern, article_UK, flags=re.DOTALL)
basic_info_dic = {}
for line in basic_info:
    basic_info_dic[line[0]] = line[1]

for k, v in basic_info_dic.items():
    print(f'key = {k}, value = {v}')
