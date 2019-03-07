'''  ファイル参照の抽出 '''
# 記事から参照されているメディアファイルをすべて抜き出せ．
import re
import json
min_lv = lv = 1
file_name = 'article_UK.json'

with open(file_name, "r") as f:
    article_UK = json.load(f)

m_file_pattern = r'(?:File|ファイル):(.+?)\|'
media_files = re.findall(m_file_pattern, article_UK)

print('\n'.join(media_files))
