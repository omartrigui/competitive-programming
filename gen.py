"""
Random Test Case Generator for Stress Testing

This script generates random test cases for use with brute force stress testing scripts.
Modify the logic in the 'generate_test_case()' function to fit your problem's input format.

Usage:
    python gen.py

Output:
    Prints a single test case to stdout in the required input format.

Example (for a graph problem):
    1
    5 3
    1 2
    2 3
    4 5

Template:
    - Adjust n, m, and the structure as needed for your problem.
    - Use random module for randomness.
"""

import random


def generate_test_case():
    n = random.randint(2, 8)  # Number of nodes (adjust as needed)
    m = random.randint(0, n * (n - 1) // 2)  # Number of edges (adjust as needed)
    pairs = set()
    while len(pairs) < m:
        x = random.randint(1, n)
        y = random.randint(1, n)
        if x != y:
            pairs.add((min(x, y), max(x, y)))
    print(1)
    print(n, m)
    for x, y in pairs:
        print(x, y)


if __name__ == "__main__":
    generate_test_case()
