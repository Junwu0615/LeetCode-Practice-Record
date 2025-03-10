class RecentCounter:

    def __init__(self):
        self.ret = []

    def ping(self, t: int) -> int:
        self.ret += [t]
        while self.ret[0] < t - 3000:
            self.ret.pop(0)
        return len(self.ret)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)