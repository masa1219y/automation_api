import time
import tweepy
import openai

# API情報を記入
API_KEY="your api_key"
API_SECRET="api_secret"
ACCESS_TOKEN="your access_token"
ACCESS_TOKEN_SECRET="your access_token_secret"


# Chatgptのレスポンスを取得する。

def get_openai_response(messages_array):
    for item in messages_array:
        print(item)
    openai.api_key = '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'  # 発行したAPIキーを入力
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=1000,
        messages=messages_array
    )
    
    response_text = response["choices"][0]["message"]["content"].replace(
        '/n', '')

    return response_text

#クライアント関数を作成
def ClientInfo():
    client=tweepy.Client(consumer_key=API_KEY,
                         consumer_secret=API_SECRET,
                         access_token=ACCESS_TOKEN,
                         access_token_secret=ACCESS_TOKEN_SECRET,
                         )
    
    return client

while (True):
    try:
        past_content = "python"

        content =( '''''
                  #命令書:
                  あなたはネットビジネスで大きな成果を出している人です。
                  あなたのツイッターは人気で１０万人以上のフォロワーがいます。
                  以下の制約条件と入力文をもとに、バズりそうなツイートを考えてください。
                #制約条件:
                ・文字数は全角文字で１１０文字以上、１４０文字以内
                ・文章を簡潔に。
                ・友達に話書けるような言葉で。
                ・#タグは使わないこと。
                ・入力文のキーワードは出力文には入れないこと。
                ・毎回入力する度にカテゴリと内容は変えること。

                #入力文:
                やる気が出ない時に見るとテンションの上がる励まし
               
                #出力文:"
                ''''')        
        
        messages_array = []
        messages_array.append({"role": "system", "content": past_content})
        messages_array.append({"role": "user", "content": content})

        response = get_openai_response(
            messages_array).replace("「", "").replace("」", "")

        print(response)
        # ツイートする。
        tweet = ClientInfo().create_tweet(text=response)
        time.sleep(43200)
    except Exception:
        print("エラーが起こりました。もう1度ChatGPTへリクエストから始めます。")
        time.sleep(3)

