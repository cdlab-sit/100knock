''' 共参照解析 '''
# Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を
# 代表参照表現（representative mention）に置換せよ．ただし，置換するときは，
# 「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．．

from xml.etree import ElementTree as ET
import glob


def main():
    file_name = '**/nlp.txt.xml'
    names = replace_coreference(glob.glob(file_name, recursive=True)[0])
    # show_doc(glob.glob(file_name, recursive=True)[0])
    # print(names)


def replace_coreference(file_name):
    root = ET.parse(file_name).getroot()
    coreference_iter = root[0].find('coreference')
    print(type(coreference_iter))
    for coreference in coreference_iter.findall('coreference'):
        print(coreference[0].findtext('text'))
        print('a')
    return 


def show_doc(file_name):

    root = ET.parse(file_name).getroot()
    sentences_iter = root.iter('sentence')
    a = []
    for sentence in sentences_iter:
        a.append(' '.join([word.text for word in sentence.iter('word')]))

    print('\n\n'.join(a))

if __name__ == '__main__':
    main()

# java -cp "*" -Xmx5g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,cleanxml,ssplit,pos,lemma,ner,parse,dcoref -ssplit.eolonly -file nlp.txt 