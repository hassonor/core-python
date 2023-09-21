### Python Logging

* Captures and records events while app is running
* Useful debugging feature
    * Not always practical to debug in real time
* Events can be categorized for easier analysis
* Provides transaction record of a program's execution
* Highly customizable output

#### Using the logging Module

```python
import logging

logging.debug("debug-level message")
logging.info("info-level message")
logging.warning("warning-level message")
logging.error("error-level message")
logging.critical("critical-level message")
```

| Message Level | Logging API          | Description                                         |
|---------------|----------------------|-----------------------------------------------------|
| DEBUG         | `logging.debug()`    | Detailed information for diagnostic purposes        |
| INFO          | `logging.info()`     | Confirmational messages indicating normal operation |
| WARNING       | `logging.warning()`  | Indication of some problem that is not severe       |
| ERROR         | `logging.error()`    | An issue that needs attention but is not critical   |
| CRITICAL      | `logging.critical()` | Severe error indicating an inability to proceed     |

#### Customized Logging

| Format String     | Description                                                                                             |
|-------------------|---------------------------------------------------------------------------------------------------------|
| `%(asctime)s`     | Human-readable time when the LogRecord was created. Can be configured to display in different formats.  |
| `%(created)f`     | Time when the LogRecord was created, represented as a floating-point number in seconds since the epoch. |
| `%(filename)s`    | Filename portion of the pathname where the logging call was issued.                                     |
| `%(funcName)s`    | Name of the function containing the logging call.                                                       |
| `%(levelname)s`   | Text logging level for the message (`'DEBUG'`, `'INFO'`, `'WARNING'`, `'ERROR'`, `'CRITICAL'`).         |
| `%(levelno)s`     | Numeric logging level for the message (e.g., `DEBUG` is 10).                                            |
| `%(lineno)d`      | Source line number where the logging call was issued.                                                   |
| `%(message)s`     | The logged message. Can be a computed string or formatted text depending on the logging call.           |
| `%(module)s`      | Module name portion of the filename where the logging call was issued.                                  |
| `%(name)s`        | Name of the logger used to log the call.                                                                |
| `%(pathname)s`    | Full pathname of the source file where the logging call was issued.                                     |
| `%(process)d`     | Process ID (PID) where the logging call was issued.                                                     |
| `%(processName)s` | Name of the process under which the logging call was issued.                                            |
| `%(thread)d`      | Thread ID where the logging call was issued.                                                            |
| `%(threadName)s`  | Name of the thread under which the logging call was issued.                                             |
