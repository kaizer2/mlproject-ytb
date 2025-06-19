import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', LOG_FILE)
os.makedirs(os.path.dirname(logs_path), exist_ok=True)


LOG_FILE_PATH = os.path.join(os.getcwd(), LOG_FILE)

logging.basicConfig(
    filename=logs_path,
    format = "[%(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)


    