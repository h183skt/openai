from linebot import LineBotApi, WebhookHandler

# チャンネルシークレットとチャンネルアクセストークンを設定
channel_secret = os.environ["CHANNEL_SECRET"]
channel_access_token = os.environ["CHANNEL_ACCESS_TOKEN"]

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

from gpt_response_generator import generate_response

from linebot.models import TextMessage, TextSendMessage

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    gpt_response = generate_response(user_message)
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=gpt_response))

    from flask import Flask, request, abort

app = Flask(__name__)

# Webhookのエンドポイントを設定
@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except Exception as e:
        abort(400)

    return "OK"

if __name__ == "__main__":
    app.run()