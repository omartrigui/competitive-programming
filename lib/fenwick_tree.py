class FenwickTree:
    def __init__(self, size):
        self.n = size + 2
        self.tree = [0] * self.n
        self.B1 = [0] * self.n
        self.B2 = [0] * self.n

    def add(self, i, val):
        while i < self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    def _add(self, bit, i, val):
        while i < self.n:
            bit[i] += val
            i += i & -i

    def range_add(self, l, r, val):
        self._add(self.B1, l, val)
        self._add(self.B1, r + 1, -val)
        self._add(self.B2, l, val * (l - 1))
        self._add(self.B2, r + 1, -val * r)

    def _query(self, bit, i):
        res = 0
        while i > 0:
            res += bit[i]
            i -= i & -i
        return res

    def prefix_sum(self, i):
        return self._query(self.B1, i) * i - self._query(self.B2, i)

    def suffix_sum(self, i):
        return self.prefix_sum(self.n - 2) - self.prefix_sum(i - 1)
