def roman_to_int(s: str) -> int:
    SYMBOLS = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    VALUES = [1, 5, 10, 50, 100, 500, 1000]
    SYMBOL_TO_VALUE = dict(zip(SYMBOLS, VALUES))

    total = 0
    prev_value = 0

    for ch in reversed(s):
        current_value = SYMBOL_TO_VALUE[ch]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total
