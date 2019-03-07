''' カテゴリ名を含む行を抽出 '''
# 記事中でカテゴリ名を宣言している行を抽出せよ．

import json
from os.path import dirname, join

with open(join(dirname(__file__), 'article_UK.json'), "r") as f:
    article_UK = json.load(f)

article_UK_list = article_UK.split()
Category_line = []
for line in article_UK_list:
    if 'Category' in line:
        Category_line.append(line)

print('\n'.join(Category_line))
