import sqlite3

# データベースに接続
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# データの挿入
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Alice", 30))
conn.commit()

# データの取得
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()
print(users)

# OpenAIのライブラリをインストール
pip install openai

import openai

# APIキーの設定
openai.api_key = 'your-api-key'

# メッセージの送信と応答の取得
def get_chatgpt_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# プロンプトを送信して応答を取得
response = get_chatgpt_response("Hello, how are you?")
print(response)

# データベースからユーザー情報を取得
cursor.execute("SELECT name FROM users WHERE id = 1")
user = cursor.fetchone()

# ChatGPTにプロンプトを送信
if user:
    prompt = f"Hello {user[0]}, how can I assist you today?"
    response = get_chatgpt_response(prompt)
    print(response)
    