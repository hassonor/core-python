class LoggingContextManager:
    def __enter__(self):
        print('LoggingContextManger.__enter__()')
        return "We are in a with-block!"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('LoggingContextManger.__exit__({},{},{})'.format(exc_type, exc_val, exc_tb))
        return


with LoggingContextManager() as x:
    print("x = ", x)
