import socket
import json
import os

class Constants():

    if 'ealbiero' in socket.gethostname():
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        with open(config_path, 'r') as f:
            config = json.load(f)
        BOT_TOKEN = config.get('BOT_TOKEN', '')
        USER_ID = config.get('USER_ID', '')
    else:
        BOT_TOKEN = os.environ['BOT_TOKEN']
        USER_ID = os.environ['USER_ID']