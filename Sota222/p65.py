''' MongoDBの検索 '''
# MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．
# さらに，これと同様の処理を行うプログラムを実装せよ．

import pymongo


def main():
    result = search_Queen()
    print(result)


def search_Queen():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.artist_database
    collection = db.artist_collection
    ret = collection.find({'$and': [{'name': 'Queen'}]})
    return '\n\n'.join([str(doc) for doc in ret])

if __name__ == '__main__':
    main()
