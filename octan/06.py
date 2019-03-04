# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．


def n_gram(str, n):
    ngr_list = []

    for i in range(len(str) - n + 1):
        ngr_list.append(str[i:i + n])

    return ngr_list

X = n_gram("paraparaparadise", 2)
Y = n_gram("paragraph", 2)
print("Xの中身: ", X)
print("Yの中身: ", Y)
print("和集合: ", set(X) | set(Y))
print("積集合: ", set(X) & set(Y))
print("差集合: ", set(X) - set(Y))
print("差集合: ", set(Y) - set(X))
print("seがXに含まれているか: ", "se" in X)
print("seがYに含まれているか: ", "se" in Y)
