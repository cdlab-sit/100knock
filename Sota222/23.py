''' セクション構造 '''
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ

import json
import re
import pprint
min_lv = lv = 1
file_name = 'article_UK.json'

with open(file_name, "r") as f:
    article_UK = json.load(f)

dupli_sec = {}
while True:
    s_pattern = '={' + str(lv + 1) + '}(.*)={' + str(lv + 1) + '}'
    _change = re.findall(s_pattern, article_UK)
    dupli_sec[lv] = set(map(lambda x: x.strip('='), _change))
    if dupli_sec[lv]:
        lv += 1
    else:
        break
section = {}
for lv in range(min_lv, lv):
    section[lv] = dupli_sec[lv] - dupli_sec[lv + 1]

pprint.pprint(section)
