from math import log
from handling_exceptions import convert


def string_log(s):
    v = convert(s)
    return log(v)
