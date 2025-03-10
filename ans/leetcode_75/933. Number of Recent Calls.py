class RecentCounter:

    def __init__(self):
        self.ret = []

    def ping(self, t: int) -> int:
        temp = [-3000 + t, t]
        self.ret += [t]
        return len([i for i in self.ret if temp[0] <= i <= temp[1]])

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)