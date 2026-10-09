class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        res = []

        for i in range(len(nums)):
            n = nums[i]
            d = target - n
            if mp.get(d) != None:
                res.append(mp.get(d))
                res.append(i)
            mp[n] = i
        
        return res

    