''' 複数のドキュメントの取得 '''
# 特定の（指定した）別名を持つアーティストを検索せよ．

import pymongo


def main():
    alias = input('別名を入力してください\n:')
    result = search_alias(alias)
    print(result)


def search_alias(alias):
    client = pymongo.MongoClient('localhost', 27017)
    db = client.artist_database
    collection = db.artist_collection
    count = collection.find({'aliases.name': alias})
    return '\n\n'.join([str(doc) for doc in count])

if __name__ == '__main__':
    main()
