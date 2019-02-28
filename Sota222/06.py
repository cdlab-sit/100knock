# "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
# XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．


def n_gram(string, n):
    return [string[i: i + n] for i in range(len(string) - n + 1)]

sentences = ["paraparaparadise", "paragraph"]
sentences = [n_gram(sentence, 2) for sentence in sentences]

# これでもいけるがpep8さんに長過ぎと怒られる
# sentences = list(map(lambda x: [x[i: i + 2] for i in range(len(x) - 2 + 1)], sentences))

X = set(sentences[0])
Y = set(sentences[1])
print(X | Y)
print(X & Y)
print(X - Y)
print("'se'というbi-gramがXに含まれる => ", "se" in X)
print("'se'というbi-gramがYに含まれる => ", "se" in Y)
