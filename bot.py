from time import sleep
from gpt4free import usesless
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from os import getenv, open
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
    i = 0
    result = theb.Completion.create(
        update.message.text,
        parent_message_id=message_id[update.effective_chat.id] if update.effective_chat.id in message_id else ""
    )
    message_id[update.effective_chat.id] = next(result)['id']
    for data in result:
        text += data['delta']
        if i % 20 == 0:
            try:
                msg = await msg.edit_text(text)
            except Exception:
                print("Error = " + Exception)
        i += 1
    if len(msg.text) != len(text):
        try:
            await msg.edit_text(text)
        except Exception:
            print("text: ", text, "prev: ", msg.text)


if __name__ == "__main__":
    app = ApplicationBuilder().token(getenv("tg_token")).build()
    app.add_handler(MessageHandler(None, echo))
    app.run_polling()