''' オブジェクトを値に格納したKVS '''
# KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）の
# リストを検索するためのデータベースを構築せよ．
# さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
import plyvel
import gzip
import json


def main():
    file_name = 'artist.json.gz'
    artist_db = set_tag_db(file_name)
    # artist = input('検索するアーティスト名を入力してください\n:')
    artist = 'Oasis'
    search_tag(artist_db, artist)


def set_tag_db(file_name):
    artist_db = plyvel.DB('artist_tags_db', create_if_missing=True)
    with gzip.open(file_name, "r") as f_file:
        for line in f_file:
            data = json.loads(line)
            if 'name' in data and 'tags' in data:
                tags = json.dumps(data.get('tags'))
                artist_db.put(data.get('name').encode('utf-8'),
                              tags.encode('utf-8'))
    artist_db.close()
    return 'artist_tags_db'


def search_tag(tags_db, artist):
    db = plyvel.DB(tags_db, create_if_missing=True)
    for k, v in db.iterator():
        if k == artist.encode():
            tags = json.loads(v.decode())
            for tag in tags:
                print(tag)
    db.close()


if __name__ == '__main__':
    main()
