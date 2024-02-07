"""
Dict Comprehensions
{
    key_expr(item) : value_expr(item)
    for item in iterable
}

Dictionary comprehensions don't work directly on dict sources.
Use dict.items() to get keys and values from dict sources.
"""
import os
import glob

files_sizes = {os.path.relpath(p): os.stat(p).st_size for p in glob.glob('*.py')}
print(files_sizes)

country_to_capital = {'USA': 'Washington', 'Israel': 'Jerusalem', 'Morocco': 'Rabat', 'Sweden': 'Stockholm'}
print(country_to_capital)

capital_to_country = {capital: country for country, capital in country_to_capital.items()}
print(capital_to_country)
