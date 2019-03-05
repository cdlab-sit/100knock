# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．


def n_gram(string, n):
    ngram_list = []

    for count in range(len(string) - n + 1):
        ngram_list.append(string[count:count + n])

    return ngram_list

X = set(n_gram("paraparaparadise", 2))
Y = set(n_gram("paragraph", 2))
union = X | Y
intersection = X & Y
difference_XY = X - Y
difference_YX = Y - X
include_inX = "se" in X
include_inY = "se" in Y

print("Xの中身: ", X)
print("Yの中身: ", Y)
print("和集合: ", union)
print("積集合: ", intersection)
print("差集合 X-Y: ", difference_XY)
print("差集合 Y-X: ", difference_YX)
print("seがXに含まれているか: ", include_inX)
print("seがYに含まれているか: ", include_inY)
