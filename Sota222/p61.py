''' KVSの検索 '''
# 60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．import gzip

import json
import plyvel


def main():
    file_name = 'artist_db'
    artist_name = input('検索したいアーティスト名を入力してください\n:')
    area = search_artist(file_name, artist_name)
    print(area)


def search_artist(file_name, artist_name):
    artist_db = plyvel.DB(file_name, create_if_missing=True)
    area = artist_db.get(artist_name.encode('utf-8'))
    artist_db.close()
    print(type(area))
    return area

if __name__ == '__main__':
    main()
