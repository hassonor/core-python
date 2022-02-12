def length_of_longest_substring(s):
    ans = 0
    sub = ''
    for ch in s:
        if ch not in sub:
            sub += ch
            ans = max(ans, len(sub))

        else:
            cut = sub.index(ch)
            sub = sub[cut + 1:] + ch
    return ans


print(length_of_longest_substring("abcdabcd"))  # -> 4
print(length_of_longest_substring("vvvvv"))  # -> 1
