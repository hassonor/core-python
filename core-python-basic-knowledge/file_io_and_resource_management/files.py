"""
open()
-> Open a file for reading or writing
-> file: the path to the file (required)
-> mode: read, write, or append, plus binary or text
-> encoding: encoding to use in text mode

open() Modes
Mode 'r' -> open for reading
Mode 'w' -> open for writing
Mode 'a -> open for appending
Selector 'b' -> binary mode
Selector 't' -> text mode

e.g:
'wb' -> Open for writing in binary mode
'at' -> Open for appending in text mode

open() -> returns a file-like object.

write()
-> returns the number of codepoints written. Don't sum these values to determine file length.
"""

import sys

# Write File
f = open('write_to_file.txt', mode='wt', encoding='utf-8')
f.write('What are the roots that clutch, ')
f.write('what branched grow\n')
f.write('Out of this stony rubbish? ')
f.close()

# Read File
g = open('write_to_file.txt', mode='rt', encoding='utf-8')
print(g.read(32))
print(g.read())

g.seek(0)  # move back the point of the pointer to the start of the file

print(g.readline())
print(g.readline())

g.seek(0)
print(g.readlines())  # read to list of lines

g.close()

# Appending text File
h = open('write_to_file.txt', mode='at', encoding='utf-8')
h.writelines(
    ['Son of man, \n', 'You cannot say, or guess, ',
     'for you know only,'
     ' \n', 'A heap of broken images, '
            's', 'where the sub beats\n'])
h.close()

# File Iteration
test_file = open(sys.argv[1], mode='rt', encoding='utf-8')
for line in test_file:
    sys.stdout.write(line)
test_file.close()

"""
with-block
-> Control flow structure for managing resources
-> Can be used with any objects - such as files - which support the context-manager protocol
"""
