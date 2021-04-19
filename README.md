# notion-to-twitter

## 概要
notionの指定したページのリストを取得し、新規に追加されたアイテムの内容を自動でTweetする
Get a list of "notion", and automatically tweet onto the timeline if there are new item.

## 環境
- Python 3.x
- Google Cloud Platform ( Cloud Function, Cloud Storage, Cloud Scheduler )

## 実行方法
1. twitterとnotionのTOKENを取得し、credential_twitter.json, credential_notion.json にそれぞれ記述
2. Google Cloud Functionにファイルを追加。トリガーはPub/Sub、エントリポイントをmainに指定
3. Google Cloud Storageにmain.py中で指定したbucket名、blob名でタイトル保存用のcsvファイルを作成
4. Google Cloud Schedulerに、1のPub/Sub トリガーを呼び出す
