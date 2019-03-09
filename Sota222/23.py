''' セクション構造 '''
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ


import gzip
import json
import re


def main():
    """main関数"""
    file_name = 'jawiki-country.json.gz'
    article_name = 'イギリス'
    article_UK = get_article(file_name, article_name)
    sections = get_section(article_UK)
    print(sections)


def get_article(file_name, article_name):
    """引数file_nameのファイルを開き、article_nameの記事を抽出する関数

    Arguments:
        file_name {str} -- 対象のファイル名
        article_name {str} -- 抽出する記事名

    Returns:
        str -- 対象の記事
    """
    with gzip.open(file_name, "r") as f_file:
        for line in f_file:
            article = json.loads(line)
            if article['title'] == article_name:
                article_UK = article['text']
                break
    return article_UK


def get_section(article_UK):
    """記事中に含まれるセクション名とそのレベルを得る関数

    Arguments:
        article_UK {str} -- 対象の記事名

    Returns:
        str -- セクション名とそのレベル
    """
    min_lv = lv = 1
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
        for section in list(dupli_sec[lv] - dupli_sec[lv + 1]):
            sections[section] = lv
    return '\n'.join([f'{sec}: {lv}' for sec, lv in sections.items()])

if __name__ == '__main__':
    main()
