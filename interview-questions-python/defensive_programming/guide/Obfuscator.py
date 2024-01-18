import random
import string
from io import BytesIO
from tokenize import tokenize


class Obfuscator:
    def apply(self, code):
        pass

    def setRand(self, r):
        self.rand = r

    def getRand(self):
        return self.rand

    @staticmethod
    def makeRandVar():
        newvar = '' + random.choice(string.ascii_letters)
        for i in range(random.randint(5, 10)):
            newvar += random.choice(string.digits + string.ascii_letters)

        return newvar


class LineObfuscator(Obfuscator):
    def apply(self, code):
        self.setRand(random.randint(0, len(code) - 1))
        lineIndex = self.getRand()
        newline = ''
        i = 0
        while code[lineIndex][i] == ' ':
            newline += ' '
            i += 1
        randVar = Obfuscator.makeRandVar()
        newline += randVar + ' = ' + \
                   str(random.randint(1, 1000)) + \
                   random.choice(['+', '-', '*', '/']) + \
                   str(random.randint(1, 100))
        code.insert(lineIndex + 1, newline)
        return code


class VarObfuscator(Obfuscator):
    def apply(self, code):
        newcode = []
        counter = self.getRand()
        while True:
            for line in code:
                g = tokenize(BytesIO(line.encode('utf-8')).readline)
                previous = ''
                for toknum, tokval, tokbeg, tokend, tokline in g:
                    if tokval == '=':
                        counter -= 1
                        if counter == 0:
                            break
                    previous = tokval
                if counter == 0:
                    while True:
                        newvar = Obfuscator.makeRandVar()
                        found = False
                        for line in code:
                            if newvar in line:
                                found = True
                                break
                        if not found:
                            break
                    for line in code:
                        line = line.replace(previous, newvar)
                        newcode.append(line)
                    return newcode


class MultivarObfuscator(VarObfuscator):
    def __init__(self, repetition):
        self.repeat = repetition

    def apply(self, code):
        LINE_VAR_LIMIT = 10
        for i in range(self.repeat):
            self.setRand(random.randint(1, len(code)) * LINE_VAR_LIMIT)
            code = VarObfuscator.apply(self, code)
        return code


if __name__ == '__main__':
    a = LineObfuscator()
    b = VarObfuscator()
    b.setRand(15)
    c = MultivarObfuscator(5)
    c.setRand(15)
    code = ['def f():',
            ' print("hello")',
            ' number1 = 100',
            ' number2 = 200',
            ' print(number1 + number2)']
    obfuscators = [a, b, c]
    for obs in obfuscators:
        code = obs.apply(code)
        for line in code:
            print(line)

    c.textField = "some text"
    print(dir(c))
    c.getRand = c.setRand
    c.getRand(21)
    print(c.__class__)
    print(c.__class__.__dict__.items())
