''' テンプレートの抽出 '''
# 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
# 辞書オブジェクトとして格納せよ．
import re
import json
file_name = 'article_UK.json'

with open(file_name, "r") as f:
    article_UK = json.load(f)

basic_pattern = r'{{基礎情報(.+?)}}\n'
basic_info_s = re.search(basic_pattern, article_UK, flags=re.DOTALL)
print(basic_info_s.group())
basic_info_str = str(basic_info_s)

basic_pattern = r'\|(.+?) = (.+?)\n'
basic_info_f = re.findall(basic_pattern, basic_info_s.group(), flags=re.DOTALL)
print(basic_info_f)  # 最下のがない
print()

