# import shutil
# import argparse
# import smtplib
import glob
import os
import sys
import re
import math
import random
import statistics
from urllib.request import urlopen
from datetime import date
import zlib
from timeit import Timer

# 10.1: Operating System Interface
print(os.getcwd())  # Return the current working directory
os.chdir('/Users/orh/PycharmProjects/core-python/')  # Change current working directory
print(os.getcwd())
# print(os.system('mkdir today'))  # Run the command mkdir in the system shell

print(dir(os))
# print(help(os))

"""
For daily file and directory management tasks, 
the shutil module provides a higher level interface that is easier to use:
"""
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')


# 10.2: File Wildcards
print(glob.glob('*.py'))

# 10.3: Command Line Arguments
# File demo.py

print(sys.argv[0])

# parser = argparse.ArgumentParser(
#     prog='std_a',
#     description='Show lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)

"""
When run at the command line with python std_a.py --lines=5 alpha.txt beta.txt, 
the script sets args.lines to 5 and args.filenames to ['alpha.txt', 'beta.txt'].
"""

# 10.4: Error Output Redirection and Program Termination
# sys.stderr.write('Warning, log file not found starting a new one\n')

# 10.5: String Pattern Matching
print(re.findall(r'\bf[a-zA-Z]*', 'which foot or hand fell fastest fAmous'))
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))


def remove_repeated_words(text):
    pattern = r'\b([a-z]+) \1'
    # Initially, we haven't made any replacements
    replacements = 1
    while replacements:
        # Perform the substitution
        text, replacements = re.subn(pattern, r'\1', text)
    return text


input_text = 'cat in the the the the the hat hat hat'
result = remove_repeated_words(input_text)
print(result)

print('tea for too'.replace('too', 'two'))

# 10.6: Mathematics
print(math.cos(math.pi / 4))
print(math.log(1024, 2))
print(random.sample(range(100), 10))  # sampling without replacement
print(random.random())  # random float
print(random.randrange(6))  # random integer chosen from range(6)

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))  # ממוצע
print(statistics.median(data))  # חציון
print(statistics.variance(data))  # שונות

# 10.7. Internet Access
with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()  # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())  # Remove trailing newline

# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
#                 """To: jcaesar@example.org
#                 From: soothsayer@example.org
#
#                 Beware the Ides of March.
#                 """)
# server.quit()

# 10.8: Dates and Times
now = date.today()
print(now)
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
birthday = date(1964, 7, 31)
age = now - birthday
print(age.days)

# 10.9: Data Compression
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))
print(zlib.crc32(s))

# 10.1: Performance Measurement
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

print(Timer('a,b = b,a', 'a=1; b=2').timeit())
