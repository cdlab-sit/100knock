''' 検索件数の取得 '''
# MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ

import pymongo


def main():
    result = search_Queen()
    print(result)


def search_Queen():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.artist_database
    collection = db.artist_collection
    ret = collection.find({'name': 'Queen'})
    return '\n\n'.join([str(doc) for doc in ret])

if __name__ == '__main__':
    main()
