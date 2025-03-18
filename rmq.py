import sys
import itertools


class RMQ:
    def __init__(self, n):
        self.sz = 1
        self.inf = (1 << 31) - 1
        while self.sz <= n: self.sz = self.sz << 1
        self.dat = [self.inf] * (2 * self.sz - 1)

    def update(self, idx, x):
        idx += self.sz - 1
        self.dat[idx] = x
        while idx > 0:
            idx = (idx - 1) >> 1
            self.dat[idx] = min(self.dat[idx * 2 + 1], self.dat[idx * 2 + 2])

    def query(self, a, b):
        return self.query_help(a, b, 0, 0, self.sz)

    def query_help(self, a, b, k, l, r):
        if r <= a or b <= l:
            return sys.maxint
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            return min(self.query_help(a, b, 2 * k + 1, l, (l + r) >> 1),
                       self.query_help(a, b, 2 * k + 2, (l + r) >> 1, r))


if __name__ == '__main__':
    line = sys.stdin.readline()
    n, q = line.split()
    n, q = int(n), int(q)
    rmq = RMQ(n)

    for i in range(q):
        line = sys.stdin.readline()
        op, a, b = line.split()
        op, a, b = int(op), int(a), int(b)
        if op == 0:
            rmq.update(a, b)
        else:
            sys.stdout.write(str(rmq.query(a, b + 1)) + '\n')
