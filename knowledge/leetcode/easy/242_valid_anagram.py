"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Approach: Count character frequencies using a hash map.

Time Complexity: O(n)
Space Complexity: O(1) — at most 26 lowercase letters
"""

from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("a", "a") is True
    assert is_anagram("ab", "a") is False
    print("All tests passed!")
