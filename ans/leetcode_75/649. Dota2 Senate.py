class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = []
        dire = []
        n = len(senate)
        for i, p in enumerate(senate):
            if p == 'R':
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.pop(0)
            d = dire.pop(0)
            if r < d:
                radiant.append(r + n)
            else:
                dire.append(d + n)

        return "Radiant" if radiant else "Dire"