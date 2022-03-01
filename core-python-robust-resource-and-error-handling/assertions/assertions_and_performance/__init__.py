"""
Assertions and Performance:
-> Assertion cost: The SortedSet invariant checks are relatively expensive.
-> Duplication: In some cases, more checks are made than are strictly necessary.
-> Performance: While not necessarily bad, this can be detrimental to performance.

python - 0:
Use Python's -0 argument to turn on basic optimizations.
In particular, this flag disables assertions.

Side-effects in Assertions:
-> The absence or presence of assertions should not affect the correctness of your program.
-> Do not use assertion conditions that have side-effects.
"""
