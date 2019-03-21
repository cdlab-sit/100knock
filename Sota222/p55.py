''' 固有表現抽出 '''
# 入力文中の人名をすべて抜き出せ．
from xml.etree import ElementTree as ET
import glob


def main():
    file_name = '**/nlp.txt.xml'
    names = read_xml_name(glob.glob(file_name, recursive=True)[0])
    print(names)


def read_xml_name(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    names = [token.findtext("word") for token in root.iter('token')
             if token.findtext("NER") == 'PERSON']
    return '\n'.join(names)

if __name__ == '__main__':
    main()
