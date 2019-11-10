''' Webアプリケーションの作成 '''
# ユーザから入力された検索条件に合致するアーティストの情報を表示するWebアプリケーションを作成せよ．
# アーティスト名，アーティストの別名，タグ等で検索条件を指定し，アーティスト情報のリストをレーティングの高い順などで整列して表示せよ．

import pymongo
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def main():
    result = search_Queen()
    return result


def search_artist(forms):
    print('forms=',forms)
    client = pymongo.MongoClient('localhost', 27017)
    db = client.artist_database
    collection = db.artist_collection
    ret = collection.find(forms)
    ret.sort('rating.count', pymongo.DESCENDING)
    return '\n\n'.join([str(doc) for doc in ret])

@app.route('/good')
def good():
    name = "Good"
    return name

@app.route('/form')
def form():
   return render_template('form.html')

@app.route('/confirm', methods = ['POST', 'GET'])
def confirm():
    if request.method == 'POST':
        forms = request.form.to_dict()
        for key, value in list(forms.items()):
            if value == "":
                del forms[key]
    sa = search_artist(forms)
    return render_template('confirm.html', result=sa)

if __name__ == '__main__':
    app.run(debug=True)