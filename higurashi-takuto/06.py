# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．


def n_gram(sequence, n):
    return [sequence[i:i+n] for i in range(len(sequence)-n+1)]


string = ['paraparaparadise', 'paragraph']

# 普通に1個ずつ書いた方がわかりやすそう。set(n_gram('paraparaparadise', 2))
X, Y = map(set, map(n_gram, string, [2, 2]))
union = X | Y
intersection = X & Y
difference = X - Y
is_include_x = 'se' in X
is_include_y = 'se' in Y

print(X, Y, union, intersection, difference, is_include_x, is_include_y)
