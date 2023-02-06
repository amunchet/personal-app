import logging

logger = logging.getLogger("dakboard_logger")
# Set the logging level of the logger
logger.setLevel(logging.DEBUG)

# Create a handler to write log messages to the console
console_handler = logging.StreamHandler()

# Set the logging level of the console handler
console_handler.setLevel(logging.DEBUG)

# Create a formatter to specify the format of the log messages
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Attach the formatter to the console handler
console_handler.setFormatter(formatter)

# Attach the console handler to the logger
logger.addHandler(console_handler)