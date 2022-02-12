"""
Explanation:
zip function allows me to loop through each string character simultaneously, 
rather than using indexes to iterate through by unpacking the array with the wildcard.
So for each loop, 'i' would be a tuple of the 0th character, then the 1st character etc
The set function basically removes duplicates 
and tells me how many unique characters there are at that index across all strings.
If it is not equal to 1, then it implies that at least one of the characters that a given index are not the same, 
and therefore should break and return whatever the previous 'bestString' was.

To clarify with an example, if two string were passed, 'year' and 'yes', the 'i' value will appear as follows:
First iteration: i = ('y', 'y')
Second iteration: i = ('e', 'e')
Third iteration: i = ('a', 's')
The program will break after the third since there is more than one unique character found, returning 
the longest common prefix which in this case is 'ye' 
"""


def longest_common_prefix(strs):
    longest_common_prefix_string = ''

    for i in zip(*strs):
        if len(set(i)) != 1:
            break
        longest_common_prefix_string += i[0]

    return longest_common_prefix_string


print(longest_common_prefix(
    ["orhasson123123123jklafshfdjhjsdgkf", "orhasson1afsklojaslkasjf1243", "orhasson2sf;alkl;fask"]))

# Output -> orhasson
