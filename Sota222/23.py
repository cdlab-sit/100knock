''' セクション構造 '''
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ

import json
import re
min_lv = lv = 1
file_name = 'article_UK.json'

with open(file_name, "r") as f:
    article_UK = json.load(f)

dupli_sec = {}
while True:
    s_pattern = f'={{{lv + 1}}}(.*)={{{lv + 1}}}'
    _sec = re.findall(s_pattern, article_UK)
    dupli_sec[lv] = set(map(lambda x: x.strip('='), _sec))
    if dupli_sec[lv]:
        lv += 1
    else:
        break
sections = {}
for lv in range(min_lv, lv):
    sections[lv] = dupli_sec[lv] - dupli_sec[lv + 1]

for level, _section in sections.items():
    _section = ' '.join(_section)
    print(f'level{level}:\n{_section}')
