#!/usr/bin/env python

import random
import string

"""
Random Test Case Generator for Stress Testing

Usage:
    python gen.py
"""


# ------------------ Random Generators ------------------ #


def random_number_in_range(low, high):
    """Returns a random integer between low and high (inclusive)."""
    return random.randint(low, high)


def random_lowercase_string_in_range(low_len, high_len):
    """Returns a random string of lowercase letters (a-z) with length between low_len and high_len."""
    length = random.randint(low_len, high_len)
    return ''.join(random.choices(string.ascii_lowercase, k=length))


def random_string_from_charset(low_len, high_len, charset=string.ascii_letters):
    """Returns a random string with characters from 'charset', length between low_len and high_len."""
    length = random.randint(low_len, high_len)
    return ''.join(random.choices(charset, k=length))


def random_list_of_numbers(n, low, high):
    """Returns a list of 'n' random integers each between low and high (inclusive)."""
    return [random.randint(low, high) for _ in range(n)]


def random_permutation(n):
    """Returns a random permutation of numbers from 1 to n."""
    p = list(range(1, n+1))
    random.shuffle(p)
    return p


def random_tree(n):
    """Returns a list of edges representing a random tree with n nodes."""
    edges = []
    for i in range(2, n+1):
        parent = random.randint(1, i-1)
        edges.append((parent, i))
    random.shuffle(edges)
    return edges


def random_graph(n, m, directed=False, self_loops=False):
    """Returns a list of edges representing a random graph with n nodes and m edges."""
    edges = set()
    while len(edges) < m:
        u = random.randint(1, n)
        v = random.randint(1, n)
        if not self_loops and u == v:
            continue
        if not directed and (u, v) in edges or (v, u) in edges:
            continue
        edges.add((u, v))
    return list(edges)

# ------------------ Example Usage ------------------ #


def generate():
    q = random_number_in_range(1, 5)
    print(q)
    for _ in range(q):
        a = random_number_in_range(1, 2)
        s = random_string_from_charset(1, 3, charset='ab')
        print(a, s)


if __name__ == "__main__":
    generate()
