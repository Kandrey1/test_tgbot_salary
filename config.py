import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    MONGODB_HOST = os.environ.get('MONGODB_HOST')
    MONGODB_PORT = int(os.environ.get('MONGODB_PORT'))
    TG_TOKEN = os.environ.get('TG_TOKEN')
