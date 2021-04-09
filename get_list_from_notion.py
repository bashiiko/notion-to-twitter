from notion.client import NotionClient

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
token = "your token"
client = NotionClient(token_v2=token)

# Replace this URL with the URL of the page you want to edit
url = "your url"
page = client.get_block(url)

print(page.title)

# リストを取得
cv = client.get_collection_view(url)

# リストの一覧を出力
for row in cv.collection.get_rows():
    print(row.title)
    print(row.desctiption)
    print(*row.tags)

