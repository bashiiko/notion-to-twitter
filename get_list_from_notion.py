# https://gammasoft.jp/blog/schdule-running-python-script-by-serverless/

from notion.client import NotionClient
import csv

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
    print('{0}に{1}を追加しました！'.format(page.title, title))
    print('tag: {0}'.format('、'.join(tag)))
    print('コメント: {0}'.format(description))

client = NotionClient(token_v2=token)

page = client.get_block(url)

# リストを取得
cv = client.get_collection_view(url)
file_name = 'title_list.csv'
title_list = get_title_list(file_name)

# リストの一覧を出力
for row in cv.collection.get_rows():
    title, tag, description = get_item_from_notion(row)
    if title not in title_list:
        output_twitter(page, title, tag, description)
        add_title_list(file_name, title)
