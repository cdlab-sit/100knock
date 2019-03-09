''' 内部リンクの除去 '''
# 26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
# テキストに変換せよ（参考: マークアップ早見表）．

import gzip
import json
import re


def main():
    """main関数"""
    file_name = 'jawiki-country.json.gz'
    article_name = 'イギリス'
    article_UK = get_article(file_name, article_name)
    basic_infos = get_basic(article_UK)
    print(basic_infos)


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


def get_basic(article_UK):
    """引数の記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
        その辞書オブジェクトをstrに変換したものを得る

    Arguments:
        article_UK {str} -- 対象の記事

    Returns:
        str -- フィールド名と値の辞書オブジェクト
    """
    basic_pattern = r'{{基礎情報(.+?)}}\n'
    basic_infos = re.search(basic_pattern, article_UK, flags=re.DOTALL)

    basic_pattern = r'\|(.+?) = (.+?)\n'
    basic_info = re.findall(
        basic_pattern, basic_infos.group(), flags=re.DOTALL)
    basic_info_dic = {}
    for line in basic_info: 　# for で回すと\nで切られる
        print(line[1])
        _without_emp = delete_emphasis(line[1])
        _without_link = delete_link(_without_emp)
        basic_info_dic[line[0]] = _without_link

    return '\n'.join([f'{field_name}: {val}'
                      for field_name, val in basic_info_dic.items()])


def delete_emphasis(line):
    """引数の文字列から強調表現を削除する関数

    Arguments:
        line {str} -- 基礎情報の値

    Returns:
        str -- 強調表現を削除した基礎情報の値
    """
    return line.replace("'", '')


def delete_link(line):
    # print(line.translate(str. maketrans({'[': None, ']': None})))
    # print(line)
    # print(line.translate(str. maketrans({'[': None, ']': None})))
    # print(line)
    # print(re.sub(r'\[\[(.+?)\]\]', r'(.+?)', line, flags=re.DOTALL))
    return re.sub(r'\[\[(.+?)\]\]', r'(.+?)', line, flags=re.DOTALL)

if __name__ == '__main__':
    main()
