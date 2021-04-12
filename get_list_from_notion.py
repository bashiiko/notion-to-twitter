from notion.client import NotionClient
import csv

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2=token)

# Replace this URL with the URL of the page you want to edit
page = client.get_block(url)

# リストを取得
cv = client.get_collection_view(url)


def get_item_from_notion(row):
    title = row.title
    tag = row.tags
    description = row.description
    return title, tag, description

def output_twitter(page, title, tag, description):
    print('{0}に{1}を追加しました！'.format(page.title, title))
    print('tag: {0}'.format('、'.join(tag)))
    print('コメント: {0}'.format(description))


with open('title_list.csv') as f:
    reader = csv.reader(f)
    title_list = [row[0] for row in reader]

# リストの一覧を出力
for row in cv.collection.get_rows():
    title, tag, description = get_item_from_notion(row)
    if title not in title_list:
        output_twitter(page, title, tag, description)
        with open('title_list.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([title])