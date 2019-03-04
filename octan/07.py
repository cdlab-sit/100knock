# 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
# さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．


def mk_str(x, y, z):
    line = str(x) + "時の" + str(y) + "は" + str(z)
    return line

print(mk_str(12, "気温", 22.4))
