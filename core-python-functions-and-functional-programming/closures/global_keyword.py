"""
global
-> Introduces binding from the global scope into another scope
"""

message = 'global'


def enclosing():
    message = 'enclosing'

    def local():
        global message
        message = 'local'

    print('enclosing message:', message)
    local()
    print('enclosing message:', message)


print('global message:', message)
enclosing()
print('global message:', message)
