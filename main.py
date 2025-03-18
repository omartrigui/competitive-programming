#!/usr/bin/env python
import os
import random
import sys

from bisect import bisect_left, bisect_right, insort_left, insort_right
from collections import defaultdict, deque, Counter, OrderedDict
from heapq import heapify, heappop, heappush
from io import BytesIO, IOBase
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, compress
from math import gcd, floor, sqrt, pi, factorial, ceil, inf
from string import ascii_lowercase, ascii_uppercase
from types import GeneratorType
from functools import lru_cache

# sys.setrecursionlimit(10 ** 4)


def main():
    t = int(input())
    for t in range(t):
        n = int(input())

class FastIO(IOBase):
    def __init__(self, file):
        self.newlines = 0
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
        self.BUFSIZE = 8192

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, self.BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, self.BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

if os.environ.get('LOCAL') != '1':
    sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


def input():
    return sys.stdin.readline().rstrip("\r\n")


def mp():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


if __name__ == "__main__":
    main()
