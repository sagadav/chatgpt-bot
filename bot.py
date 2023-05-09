from time import sleep
from gpt4free import usesless
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from os import getenv
from dotenv import load_dotenv

load_dotenv()


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


from gpt4free import theb
message_id = {}

print("hello")
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    # user_parent_msg_id = message_id[user_id] if user_id in message_id else ""
    # req = usesless.Completion.create(
    #     prompt=update.message.text,
    #     parentMessageId=user_parent_msg_id)
    # message_id[update.effective_user.id] = req["id"]
    print(update.message.text)

    msg = await update.message.reply_text("...")
    text = ""
    prev_text = ""
    prev_text_len = 0
    i = 0
    # f'Мое имя: {update.effective_user.first_name}\nМое сообщение: ' + update.message.text
    # for token in theb.Completion.create(update.message.text):
    #     text += token
    #     print(token)
    #     if i % 15 == 0:
    #         try:
    #             msg = await msg.edit_text(text)
    #         except Exception:
    #             print("ss")
    #     i += 1
    # if len(msg.text) != len(text):
    #     try:
    #         await msg.edit_text(text)
    #     except Exception:
    #         print("text: ", text, "prev: ", msg.text)


from flask import Flask

fapp = Flask(__name__)

@fapp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app = ApplicationBuilder().token(getenv("tg_token")).build()
app.add_handler(MessageHandler(None, echo))
app.run_polling()