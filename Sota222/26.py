''' 強調マークアップの除去 '''
# 25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
# （弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
# （参考: マークアップ早見表）．
import re
import json
file_name = 'article_UK.json'

with open(file_name, "r") as f:
    article_UK = json.load(f)

basic_pattern = r'{{基礎情報(.+?)}}\n'
basic_infos = re.search(basic_pattern, article_UK, flags=re.DOTALL)

basic_pattern = r'\|(.+?) = (.+?)\n'
basic_info = re.findall(basic_pattern, basic_infos.group(), flags=re.DOTALL)


basic_info_dic = {}
for line in basic_info:
    basic_info_dic[line[0]] = line[1].replace("'", '')

for k, v in basic_info_dic.items():
    print(f'key = {k}, value = {v}')
