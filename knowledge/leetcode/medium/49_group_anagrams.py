"""
49. Group Anagrams

Given an array of strings strs, group the anagrams together.
You can return the answer in any order.

Approach: Use sorted string as key in a hash map.

Time Complexity: O(n * k log k) where k is max string length
Space Complexity: O(n * k)
"""

from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups: dict[str, list[str]] = defaultdict(list)

    for s in strs:
        key = "".join(sorted(s))
        groups[key].append(s)

    return list(groups.values())


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # Sort inner lists and outer list for comparison
    result_sorted = sorted([sorted(g) for g in result])
    expected = sorted([sorted(g) for g in [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]])
    assert result_sorted == expected

    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
    print("All tests passed!")
