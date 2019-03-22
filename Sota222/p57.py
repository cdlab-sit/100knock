''' 係り受け解析 '''
# Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を有向グラフとして可視化せよ．
# 可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
# また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．

from xml.etree import ElementTree as ET
import glob
import pydot_ng as pdt


def main():
    file_name = '**/nlp.txt.xml'
    s_id = input('有向グラフにする文章のsentence idを入力してください\n:')
    sentence2directed_graph(glob.glob(file_name, recursive=True)[0], s_id)


def sentence2directed_graph(file_name, s_id):
    dependencies = get_dependencies(file_name, s_id)
    edges = []
    dep_iter = dependencies.iter('dep')
    for dep in dep_iter:
        if dep.get('type') == 'punct':
            continue
        print(dep[0].text, dep[1].text)
        edges.append((dep[0].text, dep[1].text))
    g = pdt.graph_from_edges(edges, directed=True)
    g.write_jpeg('p57_result.jpg', prog='dot')


def get_dependencies(file_name, s_id):
    root = ET.parse(file_name).getroot()
    print(type(root))
    sentence_iter = root[0][1].iter('sentence')
    for sentence in sentence_iter:
        if sentence.get('id') == s_id:
            return sentence.find('dependencies')


if __name__ == '__main__':
    main()
