import constan as keys
from telegram.ext import *
import responses as R

print("Bot startd...")

def start_command(update, context):
    update.message.reply_text('type something random to get started!')


def help_command(update, context):
    update.message.reply_text('if you need help! you help is Google')

def bitch_command(update, context):
    update.message.reply_text('You bitch')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")





def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help",  help_command))
    dp.add_handler(CommandHandler("bitch", bitch_command))


    dp.add_handler(MessageHandler(Filters.text, handle_message))


    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()
