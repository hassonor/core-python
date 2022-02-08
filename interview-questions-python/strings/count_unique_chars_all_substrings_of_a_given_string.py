# O(N)

def unique_letter_string(s):
    res = 0
    det = 0
    first_appear = {}
    second_appear = {}

    for i in range(len(s)):
        if s[i] not in first_appear:
            det = det + i + 1
            first_appear[s[i]] = i

        elif s[i] in first_appear and s[i] not in second_appear:
            det = det + i + 1 - (first_appear[s[i]] + 1) * 2
            second_appear[s[i]] = i

        elif s[i] in first_appear and s[i] in second_appear:
            det = det + i + 1 - (second_appear[s[i]] - first_appear[s[i]]) * 2 - (first_appear[s[i]] + 1)
            first_appear[s[i]] = second_appear[s[i]]
            second_appear[s[i]] = i

        res += det

    return res
