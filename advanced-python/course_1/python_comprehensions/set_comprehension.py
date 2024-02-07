ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

ftemps1 = [(t * 9 / 5) + 32 for t in ctemps]
ftemps2 = {(t * 9 / 5) + 32 for t in ctemps}
print(ftemps1)
print(ftemps2)

stemp = "The quick brown fox jumped over the lazy dog"
chars = {c.upper() for c in stemp if not c.isspace()}
print(chars)
