''' オブジェクトを値に格納したKVS '''
# KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）の
# リストを検索するためのデータベースを構築せよ．
# さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
import plyvel
import gzip
import json


def main():
    file_name = 'artist.json.gz'
    set_tag_db(file_name)
    artist = input('検索するアーティスト名を入力してください')
    search_tag(artist)

def set_tag_db(file_name):
    artist_db = plyvel.DB('artist_tags_db', create_if_missing=True)
    with gzip.open(file_name, "r") as f_file:
        for line in f_file:
            data = json.loads(line)
            if 'tag' in data:
                tags = json.dumps(data.get('tags'))
                artist_db.put(data.get('name').encode(), tags.encode())
    artist_db.close()


def search_tag(artist):
    artist_db = plyvel.DB('artist_tags_db', create_if_missing=True)
    for k, v in artist_db.iterator():
        if k == artist.encode():
            tags = json.loads(v.decode())
        for tag in tags:
            print(tag)
    artist_db.close()


if __name__ == '__main__':
    main()
