import sys, re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians, gcd
from itertools import accumulate, permutations, combinations, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left
from heapq import heappush, heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))
sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
inf = float("inf")
vow = ['a', 'e', 'i', 'o', 'u']
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
def getKey(item): return item[0]
def sort2(l): return sorted(l, key=getKey)
def d2(n, m, num): return [[num for x in range(m)] for y in range(n)]
def isPowerOfTwo(x): return (x and (not (x & (x - 1))))
def decimalToBinary(n): return bin(n).replace("0b", "")
def ntl(n): return [int(i) for i in str(n)]
def ncr(n, r): return factorial(n) // (factorial(r) * factorial(n - r))


@lru_cache(maxsize=None)
def fibonacci(n):
    print("processing")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


sys.stdin = open(r'input/C.txt')