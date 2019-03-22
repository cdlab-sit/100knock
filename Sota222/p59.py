''' S式の解析 '''
# Stanford Core NLPの句構造解析の結果（S式）を読み込み，文中のすべての名詞句（NP）を表示せよ．
# 入れ子になっている名詞句もすべて表示すること．
from xml.etree import ElementTree as ET
import glob
import re


def main():
    file_name = '**/nlp.txt.xml'
    np_list = extract_NP(glob.glob(file_name, recursive=True)[0])
    print(np_list)


def extract_NP(file_name):
    root = ET.parse(file_name).getroot()
    parse_iter = root.iter('parse')
    np_list = []
    for parse in parse_iter:
        parse_text = parse.text
        _np_list = []
        while True:
            np = re.findall(r'^\([A-Z][A-Z]\s(\w+?)\)', parse_text)
            if np:
                _np_list.append(np[0])
            _parse_text = re.findall(r'\(.+', parse_text[1:])
            if _parse_text:
                parse_text = _parse_text[0]
            else:
                break
        np_list.append(' '.join(_np_list))
    return '\n'.join(np_list)

if __name__ == '__main__':
    main()
