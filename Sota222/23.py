''' セクション構造 '''
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ

import json
import re

min_lv = lv = 2
file_name = 'article_UK.json'

with open(file_name, "r") as f:
    article_UK = json.load(f)

s_pattern = '={' + str(min_lv) + '}(.*)={' + str(min_lv) + '}'
sec_mix = re.findall(s_pattern, article_UK)

sec_dic = {}
while True:
    print(min_lv - lv)
    sec_dic[lv] = list(filter(
        lambda x: x.strip('=') if x[lv - min_lv] != '=' else None, sec_mix
    ))
    for word in sec_mix:
        if word in sec_dic[lv]:
            sec_mix.remove(word)
            print(sec_mix)

    print(sec_dic)
    if not sec_dic[lv]:
        print('nasi')
        break
    else:
        lv += 1
print(sec_dic)
