from notion.client import NotionClient
import csv

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
token = "your token"
client = NotionClient(token_v2=token)

# Replace this URL with the URL of the page you want to edit
url = "your url"
page = client.get_block(url)

print(page.title)

# リストを取得
cv = client.get_collection_view(url)


def get_item_from_notion(row):
    title = row.title
    tag = row.tags
    description = row.description
    return title, tag, description

def output_twitter(title, tag, description):
    print(title)
    print(description)
    print(tag)


with open('title_list.csv') as f:
    reader = csv.reader(f)
    title_list = [row[0] for row in reader]

print(title_list)

# リストの一覧を出力
for row in cv.collection.get_rows():
    title, tag, description = get_item_from_notion(row)
    if title not in title_list:
        output_twitter(title, tag, description)
        with open('title_list.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([title])
    else:
        print('{0} is already added'.format(title))