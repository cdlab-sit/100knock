''' MongoDBの構築 '''
# アーティスト情報（artist.json.gz）をデータベースに登録せよ．
# さらに，次のフィールドでインデックスを作成せよ
# : name, aliases.name, tags.value, rating.value


import gzip
import json
import plyvel
import pymongo


def main():
    file_name = 'artist.json.gz'
    set_db(file_name)


def set_db(file_name):
    client = pymongo.MongoClient('localhost', 27017)
    db = client.artist_database
    collection = db.artist_collection
    print("db:", db.name)
    # collection = db.artist
    buf = []
    with gzip.open(file_name, "r") as f_file:
        i = 0
        for line in f_file:
            data = json.loads(line)
            buf.append(data)
            if i % 10000 == 0:
                collection.insert_many(buf)
                buf = []
                print('{}件追加'.format(i))
            i += 1
        if buf:
            collection.insert_many(buf)
            print('{}件追加'.format(i))

    collection.create_index([('name', pymongo.ASCENDING)])
    collection.create_index([('aliases.name', pymongo.ASCENDING)])
    collection.create_index([('tags.value', pymongo.ASCENDING)])
    collection.create_index([('rating.value', pymongo.ASCENDING)])

if __name__ == '__main__':
    main()
