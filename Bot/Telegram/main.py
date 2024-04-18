import constants as keys
from telegram.ext import * 
import Responses as R

print('Bot Started...')


def start_command(update, context):
    update.message.reply_text('Type somthing random to get started!')

def help_command(update, context):
    update.message.reply_text('If you need help! You should ask for it on Google!')

# For Responsing Normal Messages
def handle_message(update, context):

    # To Get The Message From User
    text = str(update.message.text).lower()

    response = R.sample_responses(text)

    # Bot Reply
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    # If We Use '/' Command
    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()