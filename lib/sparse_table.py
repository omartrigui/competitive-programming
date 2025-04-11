from math import floor, log2


class SparseTable:
    def __init__(self, arr, func):
        self.n = len(arr)
        self.func = func
        self.k = floor(log2(self.n)) + 1
        self.st = [[0] * self.k for _ in range(self.n)]

        for i in range(self.n):
            self.st[i][0] = arr[i]

        for j in range(1, self.k):
            for i in range(self.n - (1 << j) + 1):
                self.st[i][j] = self.func(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])

    def query(self, l, r):
        res = self.st[l][0]
        for j in reversed(range(self.k)):
            if (1 << j) <= r - l + 1:
                res = self.func(res, self.st[l][j])
                l += 1 << j
        return res
