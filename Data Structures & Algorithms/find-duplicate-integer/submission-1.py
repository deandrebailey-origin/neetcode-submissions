class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        mp = {}
        best = nums[0]
        for n in nums:
            if mp.get(n):
                mp[n] += 1
            else:
                mp[n] = 1

            if mp[best] < mp[n]:
                best = n
        return best
            
            