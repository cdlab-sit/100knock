''' 品詞タグ付け '''
# Stanford Core NLPの解析結果XMLを読み込み，単語，レンマ，品詞をタブ区切り形式で出力せよ．
from xml.etree import ElementTree as ET
import glob


def main():
    file_name = '**/nlp.txt.xml'
    pos_tag_word = read_xml(glob.glob(file_name, recursive=True)[0])
    print(pos_tag_word)


def read_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    words = [f'{token.findtext("word")}\t\
{token.findtext("lemma")}\t{token.findtext("POS")}'
             for token in root.iter('token')]
    return '\n'.join(words)

if __name__ == '__main__':
    main()
