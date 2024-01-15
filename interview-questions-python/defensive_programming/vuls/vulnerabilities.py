"""2
Security Threats  In Python:
1. Code Injection: e.g. with 'eval()'
2. Compilation of string or code file into bytecode. After that we can run it with 'exec'
3. Replace a module or a package
4. Attack the interpreter
"""

comp = input('You computer')

if not comp:
    print('error: missing input')
else:
    print('Result: ', eval(comp))

# 'import os; os.system("echo Hello, world!")'
