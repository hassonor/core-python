"""
Explanation:
The zip function allows for simultaneous iteration through each string's character by unpacking the list of strings with the wildcard.
So, in each loop, 'i' is a tuple containing the characters from all strings at the same index (0th character in the first loop, 1st character in the second loop, etc.).
The set function removes duplicates and indicates how many unique characters are at that index across all strings.
If the number of unique characters isn't 1, at least one of the strings has a different character at that index.
In such a case, we break out of the loop and return the longest common prefix found up to that point.

Example:
Consider two strings: 'year' and 'yes'.
The value of 'i' in each iteration will be:
First iteration: i = ('y', 'y')
Second iteration: i = ('e', 'e')
Third iteration: i = ('a', 's')
The loop breaks in the third iteration since there's more than one unique character.
The function will thus return the longest common prefix found up to the second iteration, which is 'ye'.
"""


def longest_common_prefix(strs):
    longest_common_prefix_string = ''

    # Iterate over characters of all strings simultaneously
    for i in zip(*strs):
        # Check if all characters in the current position are the same
        if len(set(i)) != 1:
            break
        # Add the common character to the prefix string
        longest_common_prefix_string += i[0]

    return longest_common_prefix_string


# Test the function
print(longest_common_prefix(
    ["orhasson123123123jklafshfdjhjsdgkf", "orhasson1afsklojaslkasjf1243", "orhasson2sf;alkl;fask"]))
# Output -> orhasson
