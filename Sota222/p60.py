''' KVSの構築 '''
# artist.json.gzのデータをKey-Value-Store (KVS) およびドキュメント志向型データベースに
# 格納・検索することを考える．KVSとしては，LevelDB，Redis，KyotoCabinet等を用いよ．
# ドキュメント志向型データベースとして，MongoDBを採用したが，CouchDBやRethinkDB等を用いてもよい．
import gzip
import json
import plyvel


def main():
    file_name = 'artist.json.gz'
    set_db(file_name)


def set_db(file_name):
    artist_db = plyvel.DB('artist_db', create_if_missing=True)
    with gzip.open(file_name, "r") as f_file:
        for line in f_file:
            data = json.loads(line)
            if 'name' in data and 'area' in data:
                artist_db.put(data.get('name', '').encode('utf-8'),
                              data.get('area', '').encode('utf-8'))
    artist_db.close()
if __name__ == '__main__':
    main()
