"""
nonlocal
-> Insert a name binding from an enclosing scope into the local namespace
-> Searches enclosing scopes from innermost to outermost
-> Uses the first match found
"""

message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        nonlocal message
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)


print('global message:', message)
enclosing()
print('global message:', message)
