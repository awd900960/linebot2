from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('S+ecPpxbZKaj3gBwZvml6CJWVS+4seoeTE1tcE4D0U3OWhX0psBy752WNHgVCedLp9kLLisp1F/OVQeckgwF5/wlCVabPm4xWWhH5rx+6HJf0tfKbN5EzTcdhrGS+LaG5LppPuREkSI68vn1ZqTNwQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('6279263d83be2aa65736cfd4ba5cb05e')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "很抱歉你在問甚麼?"

    if msg == 'hi':
        r = 'hi'
    elif msg == '吃飽沒'
        r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()