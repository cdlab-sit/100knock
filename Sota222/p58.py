''' タプルの抽出 '''
# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
# 「主語 述語 目的語」の組をタブ区切り形式で出力せよ．ただし，主語，述語，目的語の定義は以下を参考にせよ．
#  述語: nsubj関係とdobj関係の子（dependant）を持つ単語
#  主語: 述語からnsubj関係にある子（dependent）
#  目的語: 述語からdobj関係にある子（dependent）
from xml.etree import ElementTree as ET
import glob


def main():
    file_name = '**/nlp.txt.xml'
    extract_svo(glob.glob(file_name, recursive=True)[0])


def extract_svo(file_name):
    root = ET.parse(file_name).getroot()
    dependencie_iter = root.iter('dependencies')
    for dependencie in dependencie_iter:
        dep_list = []
        _nsubj_words = []
        _dobj_words = []
        for dep in dependencie.iter('dep'):
            d_type = dep.get('type')
            if d_type == 'punct':
                continue
            if d_type == 'nsubj' or d_type == 'dobj':
                dep_list.append((d_type, dep[0].text, dep[1].text))
                if d_type == 'nsubj':
                    _nsubj_words.append(dep[0].text) 
                else:
                    _dobj_words.append(dep[0].text)
                print('n', _nsubj_words)
                print('d',_dobj_words)
        print('end')
if __name__ == '__main__':
    main()
