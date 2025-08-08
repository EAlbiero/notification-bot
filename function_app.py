import azure.functions as func
from NotificationBot import notificationBotBp

app = func.FunctionApp()
app.register_functions(notificationBotBp)
