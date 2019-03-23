''' ソート '''
# "dance"というタグを付与されたアーティストの中でレーティングの
# 投票数が多いアーティスト・トップ10を求めよ．

import pymongo


def main():
    result = search_dance()
    print(result)


def search_dance():
    client = pymongo.MongoClient('localhost', 27017)
    db = client.artist_database
    collection = db.artist_collection
    dance_artists = collection.find({'tags.value': 'dance'})
    dance_artists.sort('rating.count', pymongo.DESCENDING)
    show = []
    for doc in dance_artists.limit(10):
        if 'rating' in doc:
            show.append(f'{doc["name"]}\t({doc["rating"]["count"]})')

    return '\n\n'.join(show)

if __name__ == '__main__':
    main()
