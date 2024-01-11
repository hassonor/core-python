import random
import string
import tokenize
import io


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
        line_index = self.getRand()
        new_line = ''
        i = 0
        while i < len(code[line_index]) and code[line_index][i] == ' ':
            new_line += ' '
            i += 1

        rand_var = Obfuscator.makeRandVar()
        new_line += rand_var + ' = ' + \
                    str(random.randint(1, 1000)) + \
                    random.choice(['+', '-', '*', '/']) + \
                    str(random.randint(1, 100))

        code.insert(line_index + 1, new_line)
        return code


class VarObfuscator(Obfuscator):
    def apply(self, code):
        new_code = []
        counter = self.getRand()
        while True:
            for line in code:
                g = tokenize.tokenize(
                    io.BytesIO(line.encode('utf-8')).readline)
                previous = ''
                for tok_num, tok_val, tok_beg, tok_end, tok_line in g:
                    if tok_val == '=':
                        counter -= 1
                        if counter == 0:
                            break
                    if counter == 0:
                        new_var = Obfuscator.makeRandVar()
                        for line in code:
                            line = line.replace(previous, new_var)
                            new_code.append(line)
                        return new_code


class MultiVarObfuscator(VarObfuscator):
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
    c = MultiVarObfuscator(5)
    c.setRand(15)
    code = ['def f(): ',
            ' print("hello")',
            ' number1 = 100',
            ' number2 = 200',
            ' print(number1 + number2)']

    obfuscators = [a, b, c]
    for obs in obfuscators:
        code = obs.apply(code)
        for line in code:
            print(line)
