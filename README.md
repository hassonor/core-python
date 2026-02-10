# Core Python Concepts & Patterns

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A comprehensive Python learning repository covering everything from fundamentals to advanced patterns, concurrency, cryptography, databases, and interview preparation. Each section contains standalone, runnable examples designed for learning and reference.

## Getting Started

```bash
# Clone the repository
git clone https://github.com/hassonor/core-python.git
cd core-python

# (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# Install dependencies (not all are needed — see requirements.txt for details)
pip install -r requirements.txt
```

Navigate to any topic directory and run examples directly:

```bash
python basic_knowledge/classes/airtravel.py
```

---

## Table of Contents

- [Core Python Basics](#core-python-basics)
- [Classes and Object-Oriented Programming](#classes-and-object-oriented-programming)
- [Functions and Functional Programming](#functions-and-functional-programming)
- [Organizing Larger Programs](#organizing-larger-programs)
- [Robust Resource and Error Handling](#robust-resource-and-error-handling)
- [Advanced Python](#advanced-python)
- [Async I/O](#async-io)
- [Parallel and Concurrent Programming](#parallel-and-concurrent-programming)
- [Cryptography (PyCryptodome)](#cryptography-pycryptodome)
- [Book Notes](#book-notes)
- [PyTorch Playground](#pytorch-playground)
- [LeetCode Solutions](#leetcode-solutions)
- [Knowledge and Interview Prep](#knowledge-and-interview-prep)
- [Environment Setup](#environment-setup)

---

## Core Python Basics

Foundational Python concepts and built-in data structures.

- [Built-in Collections](basic_knowledge/built-in-collections) — Dictionaries, Lists, Sets, Strings, Tuples
  - [Dictionaries](basic_knowledge/built-in-collections/dictionaries.py)
  - [Lists](basic_knowledge/built-in-collections/lists.py)
  - [Sets](basic_knowledge/built-in-collections/sets.py)
  - [Strings](basic_knowledge/built-in-collections/strings.py)
  - [Tuples](basic_knowledge/built-in-collections/tuple.py)
- [Binary Data](basic_knowledge/binaries) — Working with binary data and bytes
- [Classes](basic_knowledge/classes) — OOP fundamentals, flight booking system example
- [Exceptions](basic_knowledge/exceptions) — Exception handling basics
- [File I/O and Resource Management](basic_knowledge/file_io_and_resource_management) — Reading, writing, and managing files
- [Iteration and Iterables](basic_knowledge/iteration_and_iterables) — Iterators, generators, iteration protocols
- [Other Fundamentals](basic_knowledge/others) — Additional core concepts

---

## Classes and Object-Oriented Programming

Deep dive into Python's object model, inheritance, and OOP patterns.

- [Class Attributes, Methods, and Properties](classes_and_oo/class_attributes_methods_properties) — Shipping domain example
- [Class Decorators](classes_and_oo/class_decorators) — Decorator factories, location demo
- [Multiple Inheritance and MRO](classes_and_oo/multiple_inheritance_and_method_resolution_order)
  - [Method Resolution Order](classes_and_oo/multiple_inheritance_and_method_resolution_order/method_resolution_order)
  - [Multiple Inheritance](classes_and_oo/multiple_inheritance_and_method_resolution_order/multiple_inheritance)
  - [Single Inheritance and Type Inspection](classes_and_oo/multiple_inheritance_and_method_resolution_order/single_inheritance_and_type_inspection)
  - [super()](classes_and_oo/multiple_inheritance_and_method_resolution_order/super)
- [String Representation of Objects](classes_and_oo/string_representation_of_objects) — `__repr__`, `__str__`, `__format__`

---

## Functions and Functional Programming

Closures, decorators, comprehensions, and functional programming paradigms.

- [Closures](functions_and_functional_programming/closures) — Lexical scoping and closure patterns
- [Comprehensions](functions_and_functional_programming/comprehensions) — List, dict, set, and generator comprehensions
- [Decorators](functions_and_functional_programming/decorators) — Decorator mechanics, parameterized decorators
- [Extended Argument and Call Syntax](functions_and_functional_programming/extended_argument_and_call_syntax) — `*args`, `**kwargs`, unpacking
- [Functional Programming](functions_and_functional_programming/functional_programming) — `map`, `filter`, `reduce`, lambdas
- [Functions and Callables](functions_and_functional_programming/functions_and_callables) — Callable objects, first-class functions

---

## Organizing Larger Programs

Structuring Python projects with packages, modules, and plugins.

- [Implementing Plugins](organizing_larger_programs/implementing_plugins) — Plugin architecture patterns
- [Namespace and Executable Packages](organizing_larger_programs/namespace_and_executable_packages) — Namespace packages, `__main__.py`
- [Nesting Modules with Packages](organizing_larger_programs/nesting_modules_with_packages) — Package hierarchies
- [Recommended Package Layout](organizing_larger_programs/recommended_package_layout) — Standard project structure

---

## Robust Resource and Error Handling

Exception handling, context managers, assertions, and debugging.

- [Assertions](robust_resource_and_error_handling/assertions)
  - [Assertions and Performance](robust_resource_and_error_handling/assertions/assertions_and_performance)
  - [Class Invariants](robust_resource_and_error_handling/assertions/class_invariants)
  - [Postconditions and Assertions](robust_resource_and_error_handling/assertions/postconditions_and_assertions)
- [Context Managers](robust_resource_and_error_handling/context_managers)
  - [Context Manager Decorator](robust_resource_and_error_handling/context_managers/context_manager_decorator)
  - [Context Manager Protocol](robust_resource_and_error_handling/context_managers/context_manager_protocol)
  - [Implementing a Context Manager](robust_resource_and_error_handling/context_managers/implementing_a_context_manager)
  - [Database Transactions with Context Managers](robust_resource_and_error_handling/context_managers/modeling_database_transactions_with_context_managers)
  - [Multiple Context Managers](robust_resource_and_error_handling/context_managers/multiple_context_managers)
- [Exception Chaining](robust_resource_and_error_handling/exception_chaining) — Implicit and explicit chaining
- [Exception Payloads](robust_resource_and_error_handling/exception_payloads)
- [Tracebacks](robust_resource_and_error_handling/tracebacks)

---

## Advanced Python

Advanced language features, data handling, and database integration.

### Course Material
- [Built-in Functions](advanced_python/course_1/built_in_functions)
- [Classes and Objects](advanced_python/course_1/classes_and_objects)
- [Collections](advanced_python/course_1/collections)
- [Python Comprehensions](advanced_python/course_1/python_comprehensions)
- [Python Functions](advanced_python/course_1/python_functions)

### Language Features
- [Advanced Language Features](advanced_python/language_features)

### Working with Data
- [Built-in Data Functions](advanced_python/working_with_data/built_in_data_functions) — Filtering, sorting, min/max, transforms
- [Collection Classes](advanced_python/working_with_data/collection_classes) — Counter, defaultdict, deque, namedtuple
- [Python Logging](advanced_python/working_with_data/python_logging) — Basic and custom logging
- [Serialization](advanced_python/working_with_data/serialization) — JSON, CSV serialization/deserialization

### Working with Databases
- [SQLite in Python](advanced_python/working_with_databases/using_sqlite_in_python)
- [MySQL in Python](advanced_python/working_with_databases/using_mysql_in_python)
- [PostgreSQL in Python](advanced_python/working_with_databases/using_postgresql_in_python)
- [SQLAlchemy Workspaces](advanced_python/working_with_databases/) — MySQL, PostgreSQL, and SQLite with SQLAlchemy (includes Docker Compose setups)

---

## Async I/O

Asynchronous programming with `asyncio` and `aiohttp`.

- [Asyncio Demos](async_io_lib/demos_1) — `async`/`await`, `asyncio.gather`, async iterators, sync-to-async conversion
- [Async Stock Fetcher](async_io_lib/stocks) — Real-world async HTTP example with `aiohttp`

---

## Parallel and Concurrent Programming

Threading, multiprocessing, synchronization, and concurrency pitfalls.

- [Threads and Processes](parallel_and_concurrent/threads_and_processes) — Thread creation, daemon threads, process spawning
- [Locks](parallel_and_concurrent/locks) — Mutex locks, reentrant locks
- [Mutual Exclusion](parallel_and_concurrent/mutual_exclusion) — Data races, critical sections
- [Liveness](parallel_and_concurrent/liveness) — Deadlock, livelock, starvation, abandoned locks

---

## Cryptography (PyCryptodome)

Practical cryptography examples using the PyCryptodome library.

- [RSA](pycryptodome/rsa) — Key generation, encryption, decryption
- [AES-CBC](pycryptodome/aes/cbc) — AES encryption in CBC mode
- [AES-EAX](pycryptodome/aes/eax) — AES authenticated encryption
- [Hybrid RSA + AES](pycryptodome/aes_rsa) — Combining asymmetric and symmetric encryption
- [End-to-End Encryption](pycryptodome/e2e_rsa_aes_eax) — Full E2E encrypted client-server communication

---

## Book Notes

Study notes and code examples from Python books.

### Fluent Python
- [Chapter 1](book_notes/fluent_python/ch_1) — The Python Data Model (`FrenchDeck`, special methods)
- [Chapter 2](book_notes/fluent_python/ch_2) — An Array of Sequences (list comprehensions, `Vector` class)

---

## PyTorch Playground

Machine learning experiments with PyTorch and Jupyter notebooks.

- [PyTorch Playground](pytorch_playground/) — Fashion MNIST, data exploration, neural network experiments

---

## LeetCode Solutions

**42 solutions** organized by difficulty. Each includes problem description, approach, complexity analysis, and tests. [Full list](knowledge/leetcode/).

### Easy (26 problems)
| # | Problem | Approach |
|---|---------|----------|
| 1 | [Two Sum](knowledge/leetcode/easy/1_two_sum.py) | Hash map |
| 9 | [Palindrome Number](knowledge/leetcode/easy/9_palindrome_number.py) | Math |
| 20 | [Valid Parentheses](knowledge/leetcode/easy/20_valid_parentheses.py) | Stack |
| 35 | [Search Insert Position](knowledge/leetcode/easy/35_search_insert_position.py) | Binary search |
| 53 | [Maximum Subarray](knowledge/leetcode/easy/53_maximum_subarray.py) | Kadane's algorithm |
| 67 | [Add Binary](knowledge/leetcode/easy/67_add_binary.py) | Math |
| 70 | [Climbing Stairs](knowledge/leetcode/easy/70_climbing_stairs.py) | Dynamic programming |
| 83 | [Remove Duplicates from Sorted List](knowledge/leetcode/easy/83_remove_duplicates_from_sorted_list.py) | Linked list |
| 88 | [Merge Sorted Array](knowledge/leetcode/easy/88_merge_sorted_array.py) | Two pointers |
| 118 | [Pascal's Triangle](knowledge/leetcode/easy/118_pascals_triangle.py) | Dynamic programming |
| 121 | [Best Time to Buy and Sell Stock](knowledge/leetcode/easy/121_best_time_to_buy_and_sell_stock.py) | One pass |
| 136 | [Single Number](knowledge/leetcode/easy/136_single_number.py) | XOR |
| 141 | [Linked List Cycle](knowledge/leetcode/easy/141_linked_list_cycle.py) | Floyd's tortoise & hare |
| 169 | [Majority Element](knowledge/leetcode/easy/169_majority_element.py) | Boyer-Moore voting |
| 206 | [Reverse Linked List](knowledge/leetcode/easy/206_reverse_linked_list.py) | Iterative pointers |
| 226 | [Invert Binary Tree](knowledge/leetcode/easy/226_invert_binary_tree.py) | Recursion |
| 242 | [Valid Anagram](knowledge/leetcode/easy/242_valid_anagram.py) | Character counting |

...and [more easy problems](knowledge/leetcode/README.md#easy)

### Medium (11 problems)
| # | Problem | Approach |
|---|---------|----------|
| 3 | [Longest Substring Without Repeating Characters](knowledge/leetcode/medium/3_longest_substring_without_repeating.py) | Sliding window |
| 11 | [Container With Most Water](knowledge/leetcode/medium/11_container_with_most_water.py) | Two pointers |
| 15 | [3Sum](knowledge/leetcode/medium/15_three_sum.py) | Sort + two pointers |
| 33 | [Search in Rotated Sorted Array](knowledge/leetcode/medium/33_search_in_rotated_sorted_array.py) | Modified binary search |
| 36 | [Valid Sudoku](knowledge/leetcode/medium/36_valid_sudoku.py) | Hash sets |
| 49 | [Group Anagrams](knowledge/leetcode/medium/49_group_anagrams.py) | Sorted key hash map |
| 56 | [Merge Intervals](knowledge/leetcode/medium/56_merge_intervals.py) | Sort + merge |
| 102 | [Binary Tree Level Order Traversal](knowledge/leetcode/medium/102_binary_tree_level_order_traversal.py) | BFS |
| 152 | [Maximum Product Subarray](knowledge/leetcode/medium/152_maximum_product_subarray.py) | Track min/max |
| 200 | [Number of Islands](knowledge/leetcode/medium/200_number_of_islands.py) | DFS flood fill |
| 238 | [Product of Array Except Self](knowledge/leetcode/medium/238_product_of_array_except_self.py) | Prefix/suffix products |

### Hard (5 problems)
| # | Problem | Approach |
|---|---------|----------|
| 23 | [Merge k Sorted Lists](knowledge/leetcode/hard/23_merge_k_sorted_lists.py) | Min-heap |
| 42 | [Trapping Rain Water](knowledge/leetcode/hard/42_trapping_rain_water.py) | Two pointers |
| 76 | [Minimum Window Substring](knowledge/leetcode/hard/76_minimum_window_substring.py) | Sliding window |
| 124 | [Binary Tree Maximum Path Sum](knowledge/leetcode/hard/124_binary_tree_maximum_path_sum.py) | DFS |
| 295 | [Find Median from Data Stream](knowledge/leetcode/hard/295_find_median_from_data_stream.py) | Two heaps |

---

## Knowledge and Interview Prep

Interview questions, algorithms, and practical Python knowledge.

- [Algorithms](knowledge/algorithms) — Algorithm implementations
- [Arrays](knowledge/arrays) — Array-based interview questions
- [Strings](knowledge/strings) — String manipulation problems
- [Defensive Programming](knowledge/defensive_programming) — Security, sockets, SSL, vulnerability awareness
- [Flask](knowledge/flask) — Flask web framework project
- [Other Topics](knowledge/others) — Miscellaneous Python knowledge

---

## Environment Setup

- [Environment Setup Guide](install_steps/ENVIRONMENT_SETUP.md) — Python installation and environment configuration

---

## Project Structure

```
core-python/
├── advanced_python/          # Advanced features, databases, serialization
├── async_io_lib/             # Async/await, asyncio, aiohttp
├── basic_knowledge/          # Python fundamentals
├── book_notes/               # Book study notes (Fluent Python)
├── classes_and_oo/           # Object-oriented programming
├── functions_and_functional_programming/  # Closures, decorators, FP
├── install_steps/            # Environment setup guides
├── knowledge/                # Interview prep, algorithms, LeetCode
├── organizing_larger_programs/  # Packages, modules, plugins
├── parallel_and_concurrent/  # Threading, multiprocessing, locks
├── pycryptodome/             # Cryptography (RSA, AES)
├── pytorch_playground/       # PyTorch experiments
├── robust_resource_and_error_handling/  # Error handling, context managers
├── .cursorrules              # AI coding assistant rules
├── .editorconfig             # Editor configuration
├── .gitignore                # Git ignore rules
├── requirements.txt          # Python dependencies
├── LICENSE                   # MIT License
└── README.md                 # This file
```

## Contributing

Contributions, suggestions, and feedback are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-topic`)
3. Commit your changes (`git commit -m 'Add new topic examples'`)
4. Push to the branch (`git push origin feature/new-topic`)
5. Open a Pull Request

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

Made with passion by [hassonor](https://github.com/hassonor)
