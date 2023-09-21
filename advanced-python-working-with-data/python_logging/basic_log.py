import logging

# Configure the logging to save log messages to a file and also to show them in the console
logging.basicConfig(filename='output.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Logging at DEBUG level
logging.debug("This is a debug-level message")

# Logging at INFO level
logging.info("This is an info-level message")

# Logging at WARNING level
logging.warning("This is a warning-level message")

# Logging at ERROR level
logging.error("This is an error-level message")

# Logging at CRITICAL level
logging.critical("This is a critical-level message")
