# main.py

from logger import logger
import worker

logger.info("Main script started.")
worker.do_work()
logger.info("Main script finished.")
