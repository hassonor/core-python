"""
76. Minimum Window Substring

Given two strings s and t, return the minimum window substring of s
such that every character in t (including duplicates) is included in the window.

Approach: Sliding window with character frequency counts.

Time Complexity: O(n + m)
Space Complexity: O(m) where m is len(t)
"""

from collections import Counter


def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""

    need = Counter(t)
    have = 0
    required = len(need)
    window: dict[str, int] = {}

    result = ""
    result_len = float("inf")
    left = 0

    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1

        if char in need and window[char] == need[char]:
            have += 1

        while have == required:
            # Update result if this window is smaller
            window_size = right - left + 1
            if window_size < result_len:
                result_len = window_size
                result = s[left : right + 1]

            # Shrink from left
            left_char = s[left]
            window[left_char] -= 1
            if left_char in need and window[left_char] < need[left_char]:
                have -= 1
            left += 1

    return result


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("aa", "aa") == "aa"
    print("All tests passed!")
