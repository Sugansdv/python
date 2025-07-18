# logger.py

import logging

# Set up the logging configuration once here
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Create a logger instance
logger = logging.getLogger("MyAppLogger")
