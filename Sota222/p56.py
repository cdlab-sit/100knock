''' 共参照解析 '''
# Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を
# 代表参照表現（representative mention）に置換せよ．ただし，置換するときは，
# 「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．．

from xml.etree import ElementTree as ET
import glob


def main():
    file_name = '**/nlp.txt.xml'
    out_file_name = 'nlp.txt.changed.xml'
    replace_coreference(glob.glob(file_name, recursive=True)[0])
    show_doc(glob.glob(out_file_name, recursive=True)[0])
    # print(names)


def replace_coreference(file_name):
    root = ET.parse(file_name).getroot()
    tree = ET.ElementTree(element=root)
    coreference_iter = root[0].find('coreference')
    sentences = root[0].find('sentences')
    for coreference in coreference_iter.findall('coreference'):
        re_mention = coreference[0].findtext('text')
        for mention_info in coreference[1:]:
            mention = mention_info.findtext('text')
            sentence = int(mention_info.findtext('sentence'))
            start = int(mention_info.findtext('start'))
            end = int(mention_info.findtext('end'))
            # print(f're_mention:{re_mention} mention:{mention}')
            for i in range(start, end-1):
                sentences[sentence-1][0][i].clear()
            if sentences[sentence-1][0][start-1]:
                sentences[sentence-1][0][start-1].find('word').text = \
                                f'[{re_mention}] ({mention})'
    tree.write('nlp.txt.changed.xml')


def show_doc(file_name):

    root = ET.parse(file_name).getroot()
    sentences_iter = root[0][1].iter('sentence')
    a = []
    for sentence in sentences_iter:
        a.append(' '.join([word.text for word in sentence.iter('word')]))

    print('\n\n'.join(a))

if __name__ == '__main__':
    main()

# java -cp "*" -Xmx5g edu.stanford.nlp.pipeline.StanfordCoreNLP
# -annotators tokenize,cleanxml,ssplit,pos,lemma,ner,parse,dcoref
# -ssplit.eolonly -file nlp.txt
