class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            mask = n & (1<<i)
            if mask > 0:
                res += 1

        return res