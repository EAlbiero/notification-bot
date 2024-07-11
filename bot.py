import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, Application
from util import Util


USER_ID = 624780392
BOT_TOKEN = '7305825348:AAET1L713EcAmHg7DwfgiFM6CUEAuruZMNc'



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def autoUpdate(context: ContextTypes.DEFAULT_TYPE):

    Util.logActivity("Starting hourly updates check")
    msg = ""

    updates = Util.checkForUpdates()
    if updates:
        data = Util.getData()
        for u in updates:
            msg += f"Lançamento de {u}: {data['manga'][u]['url']+str(data['manga'][u]['chapter']-1)}\n"
    if msg:
        await context.bot.send_message(chat_id=USER_ID, text=msg)
    return None
    
async def checkUpdates(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.chat_id != USER_ID:
        await update.message.reply_text("Usuário inválido")
        return

    Util.logActivity("Received update request via user command. Looking for new updates")
    msg = ""

    updates = Util.checkForUpdates()
    if updates:
        data = Util.getData()
        for u in updates:
            msg += f"Lançamento de {u}: {data['manga'][u]['url']+str(data['manga'][u]['chapter']-1)}\n"
    else:
        msg = "Nenhum capítulo novo encontrado."

    await context.bot.send_message(chat_id=USER_ID, text=msg)

async def post_init(application: Application) -> None:
    application.job_queue.run_repeating(autoUpdate, 3600)


if __name__ == '__main__':

    application = Application.builder().token(BOT_TOKEN).post_init(post_init).build()

    check_update_handler = CommandHandler("att", checkUpdates)
    application.add_handler(check_update_handler)
    
    application.run_polling()