class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}

        for n in nums:
            if mp.get(n):
                return True
            mp[n] = 1
        
        return False