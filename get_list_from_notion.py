from google.cloud import storage
from tweet_on_timeline import Twitter

class GoogleCloudStorage():
    def __init__(self, bucket_name):
        storage_client = storage.Client()
        self.bucket = storage_client.bucket(bucket_name)

    def read_file(self, file_name):
        blob = self.bucket.blob(file_name)
        content = blob.download_as_text() # content:str
        return content.splitlines() # 改行文字で分割

    def write_file(self, file_name, content):
        blob = self.bucket.blob(file_name)
        blob.upload_from_string(content)

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
    message = '\n'.join(message)
    return message


def main(event, context):

    credential_notion_path = "credential_notion.json" # notionのトークンとURL
    credential_notion = open(credential_notion_path, "r")
    credential_notion_load = json.load(credential_notion)
    
    token  = credential_notion_load["TOKEN"]
    url = credential_notion_load["URL"]
    client = NotionClient(token_v2=token)

    # page = client.get_block(url)

    #notionのリストを取得
    cv = client.get_collection_view(url)

    bucket_name = "title_list"
    source_blob_name = "title_list.csv"
    gcs = GoogleCloudStorage(bucket_name)
    title_list = gcs.read_file(source_blob_name)

    credential_data_path = "credential_twitter.json" # Twitterのトークンなど
    twitter = Twitter(credential_data_path)

    # リストの一覧を出力
    for row in cv.collection.get_rows():
        title, tag, description = get_item_from_notion(row)
        if title not in title_list:
            title_list.append(title)
            message = output_twitter(page, title, tag, description)
            twitter.tweet(message)

    title_list = '\n'.join(title_list)
    gcs.write_file(source_blob_name, title_list)

