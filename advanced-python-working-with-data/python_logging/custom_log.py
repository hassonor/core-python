import logging


def another_function():
    logging.debug("This is a debug level log message", extra=ext_data)


fmtstr = "User: %(user)s %(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
datestr = "%m/%d/%Y %I:%M:%S %p"
ext_data = {"user": "hassonor@gmail.com"}

logging.basicConfig(filename='output.log', level=logging.DEBUG, format=fmtstr, datefmt=datestr)

# Logging at DEBUG level
logging.debug("This is a debug-level message", extra=ext_data)

# Logging at INFO level
logging.info("This is an info-level message", extra=ext_data)

# Logging at WARNING level
logging.warning("This is a warning-level message", extra=ext_data)

# Logging at ERROR level
logging.error("This is an error-level message", extra=ext_data)

# Logging at CRITICAL level
logging.critical("This is a critical-level message", extra=ext_data)

another_function()
