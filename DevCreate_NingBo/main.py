from data_processing import process_data
from api_client import send_request
import logging
from logger import setup_logging
from task_executor import execute_tasks
from config import Config

setup_logging()
df = process_data(Config.EXCEL_PATH)
print(df)  # debug
success_count = execute_tasks(df, send_request, Config.THREADS)
logging.info(f"已成功执行{success_count}行，总行数：{len(df)}")
