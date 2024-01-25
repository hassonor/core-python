def numJewlsInStones(jewels, stones):
    counter = 0
    for ch1 in jewels:
        for ch2 in stones:
            if ch1 == ch2:
                counter += 1
    return counter
