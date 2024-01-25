from array import array
from collections import deque
import bisect
from heapq import heapify, heappop, heappush

a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

d = deque(["task1", "task2", "task3", "task4"])
d.append("task5")
print("Handling", d.popleft())

# Graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}


def breadth_first_search(start_node, goal_node, graph):
    # Initialize the deque with the starting node
    unsearched = deque([(start_node, [start_node])])  # store node and path to node

    while unsearched:
        current_node, path = unsearched.popleft()

        # Return path if goal is reached
        if current_node == goal_node:
            return path

        # Add adjacent nodes to the queue
        for neighbor in graph[current_node]:
            unsearched.append((neighbor, path + [neighbor]))

    return None  # return None if no path is found


# Perform BFS
start_node = 'A'
goal_node = 'F'
path = breadth_first_search(start_node, goal_node, graph)

if path:
    print(f"Path from {start_node} to {goal_node}: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}")

"""
the library also offers other tools such as the bisect module with functions 
for manipulating sorted lists:
"""
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
print(scores)  # [(100, 'perl'), (200, 'tcl'), (300, 'ruby'), (400, 'lua'), (500, 'python')]

"""
The heapq module provides functions for implementing heaps based on regular lists. 
The lowest valued entry is always kept at position zero. 
This is useful for applications which repeatedly access the smallest 
element but do not want to run a full list sort:
"""

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
print(data)
heapify(data)  # rearrange the list into heap order
print(data)
heappush(data, -5)  # add a new entry
print(data)
print([heappop(data) for i in range(3)])  # fetch the three smallest entries
print(data)
