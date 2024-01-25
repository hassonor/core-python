import reprlib
import pprint
import textwrap
from string import Template
import struct

# 11.1: Output Formatting
print(reprlib.repr(set('supercalifragilisticexpialidocious')))

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
                                                        'yellow'], 'blue']]]
pprint.pprint(t, width=30)

# The textwrap module formats paragraphs of text to fit a given screen width:
doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""

print(textwrap.fill(doc, width=40))

# 11.2: Templating
t = Template('${village} folks send $$10 to $cause.')
print(t.substitute(village='Tel-Aviv', cause='the Israeli fund'))

t2 = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
print(t2.safe_substitute(d))
