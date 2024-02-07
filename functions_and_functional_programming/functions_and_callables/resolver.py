import socket


class Resolver:
    """
    Arguments passed to the class object
    are forwarded to the class's __init__()
    """

    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache[host]

    @property
    def cache(self):
        return self._cache

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache
