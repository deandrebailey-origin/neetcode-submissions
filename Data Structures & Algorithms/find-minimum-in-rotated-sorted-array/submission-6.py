class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        if r == 0:
            return nums[0]
        
        while l <= r: 
            m = + l + (r - l) // 2
            print(l, m, r)
            if nums[l] < nums[m]:
                if nums[r] > nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: 
                if nums[r] > nums[m]:
                    r = m
                else:
                    l = m + 1

            

        return nums[r]
            
        

            
                