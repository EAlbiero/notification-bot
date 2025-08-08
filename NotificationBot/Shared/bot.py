import logging, sys
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, Application
from Shared.parser import Parser
from Shared.constants import Constants

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

class Bot():
    USER_ID = Constants.USER_ID

    def __init__(self):

        BOT_TOKEN = Constants.BOT_TOKEN
        self.application = Application.builder().token(BOT_TOKEN).post_init(Bot.post_init).build()

        check_update_handler = CommandHandler("att", Bot.checkUpdates)
        self.application.add_handler(check_update_handler)
        self.application.run_polling()


    async def checkUpdates(update: Update, context: ContextTypes.DEFAULT_TYPE):

        if update.message.chat_id != Bot.USER_ID:
            await update.message.reply_text("Usuário inválido")
            return

        msg = ""

        updates = Parser.checkForUpdates()
        if updates:
            data = Parser.getData()
            for u in updates:
                msg += f"Lançamento de {u}: {data['manga'][u]['url']+str(data['manga'][u]['chapter']-1)}\n"
        else:
            msg = "Nenhum capítulo novo encontrado."

        await context.bot.send_message(chat_id=Bot.USER_ID, text=msg)


    async def post_init(application: Application) -> None:
            print("checking updates")

            msg = ""

            updates = Parser.checkForUpdates()
            if updates:
                data = Parser.getData()
                for u in updates:
                    msg += f"Lançamento de {u}: {data['manga'][u]['url']+str(data['manga'][u]['chapter']-1)}\n"
            else:
                msg = "Nenhum capítulo novo encontrado."

            print(application)
            print(application.bot)
            await application.bot.send_message(chat_id=Bot.USER_ID, text=msg)
            sys.exit()








