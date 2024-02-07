class LoggingContextManager:
    def __enter__(self):
        print('LoggingContextManger.__enter__()')
        return "We are in a with-block!"

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print("LoggingContextManager.__exit__: normal exit detected")
        else:
            print('LoggingContextManger.__exit__: Exception detected! type={}, value={}, traceback={}'
                  .format(exc_type, exc_val, exc_tb))


with LoggingContextManager() as x:
    print("x = ", x)

with LoggingContextManager():
    raise ValueError()
