from functools import reduce


def count_words(doc):
    normalised_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalised_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


# print(count_words('It was the best of times, it was the worst of times.'))


def combine_counts(d1, d2):
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d


documents = ['Hey, how are you?', ' It was the best of times, it was the worst of times',
             'I do not like green eggs and ham. I do not like them, Sam-I-Am.',
             'Friends, Romans, countrymen, lend me your ears; I come to bury Caesar, not to praise him.']

counts = map(count_words, documents)
total_counts = reduce(combine_counts, counts)
print(total_counts)
