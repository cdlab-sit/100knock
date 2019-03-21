''' Tokenization '''
# Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
# また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
from xml.etree import ElementTree as ET
import glob


def main():
    file_name = '**/nlp.txt.xml'
    one_line_word = read_xml(glob.glob(file_name, recursive=True)[0])
    print(one_line_word)


def read_xml(file_name):
    tree = ET.parse(file_name)
    root = tree.getroot()
    return '\n'.join([word.text for word in root.iter('word')])

if __name__ == '__main__':
    main()

# コマンドライン上で操作するときについて
# java -cp "*" -Xmx2g edu.stanford.nlp.pipeline.StanfordCoreNLP -annotators
# tokenize,ssplit,pos,lemma,ner -file nlp.txt
# というコマンドを使ったが、-annotatorsオプションがないと OutOfMemoryError: Java heap space
# が発生。理由はわからん。
