# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．


def create_sentence(x, y, z):
    return "{}時の{}は{}".format(x, y, z)

x = 12
y = "気温"
z = 22.4
print(create_sentence(x, y, z))
