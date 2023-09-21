ctemps = [0, 12, 35, 100]
ftemps = [32, 67, 100, 213]

print(list(map(lambda t: (t - 32) * 5 / 9, ftemps)))
print(list(map(lambda t: (t * 9 / 5) + 32, ctemps)))
