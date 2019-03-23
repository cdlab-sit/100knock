''' 検索件数の取得 '''
# MongoDBのインタラクティブシェルを用いて，活動場所が「Japan」となっているアーティスト数を求めよ

import pymongo


def main():
    result = search_Japan_num()
    print(result)


def search_Japan_num():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.artist_database
    collection = db.artist_collection
    count = collection.find({'area': 'Japan'}).count()
    return count

if __name__ == '__main__':
    main()
