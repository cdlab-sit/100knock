''' 係り受け解析 '''
# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，
# その結果をneko.txt.cabochaというファイルに保存せよ．このファイルを用いて，
# 以下の問に対応するプログラムを実装せよ．
import CaboCha


def main():
    in_file_name = 'neko.txt'
    out_file_name = 'neko.txt.cabocha'
    neko_txt = read_file(in_file_name)
    result = dependency_parsing(neko_txt)
    write_result(result, out_file_name)


def read_file(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()
    return contents


def dependency_parsing(sentence):
    c = CaboCha.Parser()
    analysis_results = []
    for line in sentence.split('\n'):
        tree = c.parse(line)
        analysis_results.append(tree.toString(CaboCha.FORMAT_XML))
    return '\n'.join(analysis_results)


def write_result(result, file_name):
    with open(file_name, 'w') as f:
        f.write(result)


if __name__ == "__main__":
    main()
