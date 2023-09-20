def get_search_results(words, queries):
    anagram_dict = {}

    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)

    results = []
    for query in queries:
        sorted_query = ''.join(sorted(query))
        exist_anagrams = sorted(anagram_dict.get(sorted_query, []))

        if query in exist_anagrams:
            exist_anagrams.remove(query)

        results.append(exist_anagrams)

    return results
