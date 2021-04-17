# https://gammasoft.jp/blog/schdule-running-python-script-by-serverless/
from notion.client import NotionClient
import csv

from google.cloud import storage
from tweet_on_timeline import Twitter

def get_title_list(file_name):
    with open(file_name) as f:
        reader = csv.reader(f)
        title_list = [row[0] for row in reader]

    return title_list

def add_title_list(file_name, title):
    with open(file_name, 'a') as f:
        writer = csv.writer(f)
        writer.writerow([title])

def get_item_from_notion(row):
    title = row.title
    tag = row.tags
    description = row.description
    return title, tag, description

def output_twitter(page, title, tag, description):
    message = ['{0}に{1}を追加しました！'.format(page.title, title)]
    message.append('メモ: {0}'.format(description))
    message.append('tag: {0}'.format('、'.join(tag)))
    message.append('#積読本')
    # https://docs.python.org/ja/3/library/stdtypes.html#str.join
    message = '\n'.join(message)
    # print('{0}に{1}を追加しました！'.format(page.title, title))
    # print('tag: {0}'.format('、'.join(tag)))
    # print('コメント: {0}'.format(description))
    return message

# def main():

#     token = "1d37aa2417452b968dc7604f7a5bb4e5deae7fb6e479a241bf5a4d739fa60ead23ffd672d1e57156c5cfd3f5f063af521dc910d0c3ff0efcbb64aea9dd1a0d27d8bb28f1abd1cf531d5d2a23119d"
#     client = NotionClient(token_v2=token)

#     url = "https://www.notion.so/d01b5e64a9534cd78b2cbdaf1d8cd685?v=47bb3fe5351345a8bb00f61516378b7a"
#     page = client.get_block(url)

#     bucket_name = "title_list"
#     source_blob_name = "title_list.csv"

#     storage_client = storage.Client()

#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(source_blob_name)

#     print(blob.name)

# リストを取得
token = "1d37aa2417452b968dc7604f7a5bb4e5deae7fb6e479a241bf5a4d739fa60ead23ffd672d1e57156c5cfd3f5f063af521dc910d0c3ff0efcbb64aea9dd1a0d27d8bb28f1abd1cf531d5d2a23119d"
client = NotionClient(token_v2=token)

url = "https://www.notion.so/d01b5e64a9534cd78b2cbdaf1d8cd685?v=47bb3fe5351345a8bb00f61516378b7a"
page = client.get_block(url)

cv = client.get_collection_view(url)
file_name = 'title_list.csv'
title_list = get_title_list(file_name)

# リストの一覧を出力
for row in cv.collection.get_rows():
    title, tag, description = get_item_from_notion(row)
    if title not in title_list:
        message = output_twitter(page, title, tag, description)
        add_title_list(file_name, title)

print(message)
message = "test"
credential_data_path = "credential_twitter.json"
twitter = Twitter(credential_data_path)
twitter.tweet(message)