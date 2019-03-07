''' カテゴリ名の抽出 '''
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

import json
import re
from os.path import dirname, join

with open(join(dirname(__file__), 'article_UK.json'), "r") as f:
    article_UK = json.load(f)

c_pattern = r'\[\[Category:(.*)\]\]'
category = re.findall(c_pattern, article_UK)
category = list(map(lambda x: x.split('|')[0], category))
# 正規表現だけでできなかった...
# 他にやり方があるのかもしれない

print('\n'.join(category))
