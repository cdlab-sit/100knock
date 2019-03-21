''' 共参照解析 '''
# Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を
# 代表参照表現（representative mention）に置換せよ．ただし，置換するときは，
# 「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．．

from xml.etree import ElementTree as ET
import glob


def main():
    file_name = '**/nlp.txt.xml'
    # names = replace_coreference(glob.glob(file_name, recursive=True)[0])
    show_doc(glob.glob(file_name, recursive=True)[0])
    # print(names)


def replace_coreference(file_name):
    root = ET.parse(file_name).getroot()
    for coreferences in root.iter('coreference'):
        print(coreferences[0].findtext('end'))

    return 


def show_doc(file_name):

    root = ET.parse(file_name).getroot()
    sentences_iter = root.iter('sentence')
    for sentence in sentences_iter:
        for word in sentence.iter('word'):
            print(word.text)
        #sentence
    # print(sentence.attrib)
        # print(token.findtext('word'))
        print('----------')


if __name__ == '__main__':
    main()

# java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,cleanxml,ssplit -ssplit.eolonly,pos,lemma,ner,parse,dcoref -file nlp.txt -tokenize.whitespace -ssplit.eolonly

# java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,cleanxml,ssplit,pos,lemma,ner parse,dcoref -ssplit.eolonly -file nlp.txt 

# java -cp "*" -Xmx5g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators tokenize,cleanxml,ssplit,pos,lemma,ner,parse,dcoref -ssplit.eolonly -file nlp.txt 