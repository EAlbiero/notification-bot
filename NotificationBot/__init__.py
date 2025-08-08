import azure.functions as func
from Shared.bot import Bot

notificationBotBp = func.Blueprint()

@notificationBotBp.function_name("NotificationBot")
@notificationBotBp.timer_trigger("mytimer", schedule="0 11-22 * * *", run_on_startup=True)
def main(mytimer: func.TimerRequest) -> None:

    bot = Bot()
