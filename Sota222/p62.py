''' KVS内の反復処理 '''
# 60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．

import plyvel


def main():
    file_name = 'artist_db'
    area = search_Japan(file_name)
    print(area)


def search_Japan(file_name):
    artist_db = plyvel.DB(file_name, create_if_missing=True)
    count = 0
    for v in artist_db.iterator(include_key=False):
        if v == b'Japan':
            count += 1
    artist_db.close()
    return count

if __name__ == '__main__':
    main()
