import contextlib
import sys


@contextlib.contextmanager
def logging_context_manger():
    print('logging_context_manger: enter')
    try:
        yield "We are in a with-block!"
        print('logging_context_manger: normal exit')
    except Exception:
        print('logging_context_manger: exceptional exit', sys.exc_info())
        raise


with logging_context_manger() as x:
    print(x)

with logging_context_manger() as x:
    raise ValueError("Something went wrong!")
