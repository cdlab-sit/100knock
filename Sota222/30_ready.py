''' 形態素解析 '''
# 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をMeCabを使って形態素解析し，
# その結果をneko.txt.mecabというファイルに保存せよ．
# このファイルを用いて，以下の問に対応するプログラムを実装せよ．

# なお，問題37, 38, 39はmatplotlibもしくはGnuplotを用いるとよい．
import MeCab


def main():
    in_file_name = 'neko.txt'
    out_file_name = 'neko.txt.mecab'
    neko_txt = read_file(in_file_name)
    result = morphological_analysis(neko_txt)
    write_result(result, out_file_name)


def read_file(file_name):
    with open(file_name, 'r') as f:
        contents = f.read()
    return contents


def morphological_analysis(sentence):
    t = MeCab.Tagger('')
    return t.parse(sentence)


def write_result(result, file_name):
    with open(file_name, 'w') as f:
        f.write(result)


if __name__ == "__main__":
    main()
