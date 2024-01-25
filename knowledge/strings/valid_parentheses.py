def is_valid(s: str) -> bool:
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for ch in s:
        if ch in mapping:
            top_element = stack.pop() if stack else '#'

            if mapping[ch] != top_element:
                return False
        else:
            stack.append(ch)

    return len(stack) == 0
