''' 国旗画像のURLを取得する '''
# テンプレートの内容を利用し，国旗画像のURLを取得せよ．
# （ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
import gzip
import json
import re
import requests


def main():
    """main関数"""
    file_name = 'jawiki-country.json.gz'
    article_name = 'イギリス'
    article_UK = get_article(file_name, article_name)
    basic_info_dic = get_basic_dic(article_UK)
    image_name = re.sub(' ', '_', basic_info_dic["国旗画像"])
    national_flag_url = get_flag_url(image_name)
    print(national_flag_url)


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


def get_basic_dic(article_UK):
    """引数の記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
        その辞書オブジェクトをstrに変換したものを得る

    Arguments:
        article_UK {str} -- 対象の記事

    Returns:
        str -- フィールド名と値の辞書オブジェクト
    """
    basic_pattern = r'{{基礎情報(.+?)}}\n'
    basic_infos = re.search(basic_pattern, article_UK, flags=re.DOTALL)

    basic_pattern = r'\n\|(.+?) = (.+?)(?=\n\||}}\n)'
    basic_info = re.findall(basic_pattern, basic_infos.group(),
                            flags=re.DOTALL)
    basic_info_dic = {}
    for line in basic_info:
        _without_emp = delete_emphasis(line[1])
        _without_link = delete_link(_without_emp)
        _without_markup = delete_markup(_without_link)
        basic_info_dic[line[0]] = _without_markup
    return basic_info_dic


def delete_emphasis(line):
    """引数の文字列から強調表現を削除する関数

    Arguments:
        line {str} -- 基礎情報の値

    Returns:
        str -- 強調表現を削除した基礎情報の値
    """
    return re.sub(r"''{2,}(.+?)''{2,}", r"\1", line, flags=re.DOTALL)


def delete_link(line):
    """引数の文字列から内部リンク表現を削除する関数

    Arguments:
        line {str} -- 基礎情報の値

    Returns:
        str -- 内部リンク表現を削除した基礎情報の値
    """
    return re.sub(r"\[\[(.+?)\]\]", r'\1', line, flags=re.DOTALL)


def delete_markup(line):
    """引数の文字列からMediaWikiマークアップを削除する関数

    Arguments:
        line {str} -- 基礎情報の値

    Returns:
        str -- MediaWikiマークアップを削除した基礎情報の値
    """
    delete_bracket = re.sub(r'\[(.+?)\]', '', line, flags=re.DOTALL)
    delete_angle = re.sub(r'<br\s?/>|</?ref>', '', delete_bracket,
                          flags=re.DOTALL)
    delete_ref = re.sub(r'<ref name=(.+?)/?>', '', delete_angle,
                        flags=re.DOTALL)
    return delete_ref


def get_flag_url(image_name):
    """画像名からURLを得る関数

    Arguments:
        url {str} -- 対象となる画像名の文字列

    Returns:
        str -- 国旗画像のURL
    """
    url = "https://en.wikipedia.org/w/api.php"
    S = requests.Session()
    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": f'File:{image_name}',  # File: いるんかーい!!
        "iiprop": "url",
    }
    R = S.get(url=url, params=PARAMS)
    DATA = R.json()
    pages = DATA["query"]["pages"]
    for k in pages.keys():
        if "imageinfo" in pages[k].keys():
            flag_url = pages[k]["imageinfo"][0]["url"]
    return flag_url

if __name__ == '__main__':
    main()
