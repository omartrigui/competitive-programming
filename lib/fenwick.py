class BIT:
    def __init__(self, size):
        self.n = size + 2
        self.tree = [0] * self.n

    def add(self, i, val):
        while i < self.n:
            self.tree[i] += val
            i += i & -i

    def range_add(self, l, r, val):
        self.add(l, val)
        self.add(r + 1, -val)

    def query(self, i):
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res
