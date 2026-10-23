class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1 , 1
        temp = 0

        for i in range(n - 1):
            temp = one
            one = temp + two
            two = temp

        return one
