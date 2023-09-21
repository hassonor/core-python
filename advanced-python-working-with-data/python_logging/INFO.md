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
