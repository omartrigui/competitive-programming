class SegTree:
    # limit for array size
    N = 100002

    def __init__(self):
        self.tree = [0] * (2 * self.N)

    # function to build the tree
    def build(self, arr):
        # insert leaf nodes in tree
        for i in range(n):
            self.tree[n + i] = arr[i]

            # build the tree by calculating parents
        for i in range(n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

        # function to update a tree node

    def update_tree_node(self, p, value):
        # set value at position p
        self.tree[p + n] = value
        p = p + n

        # move upward and update parents
        i = p

        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

        # function to get sum on interval [l, r)

    def query(self, l, r):
        res = 0

        # loop to find the sum in the range
        l += n
        r += n

        while l < r:

            if l & 1:
                res += self.tree[l]
                l += 1

            if r & 1:
                r -= 1
                res += self.tree[r]

            l >>= 1
            r >>= 1

        return res


if __name__ == "__main__":
    n = 60
    s = SegTree()
    s.build([0] * n)
    # s.update_tree_node(idx, 1)
    # s.query(p1, p2 + 1)
