class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        n = len(s)
        mp = {}
        maxK = 0
        maxR = 0


        for r in range(n):   
            
            if s[r] not in mp:
                mp[s[r]] = 1
            else:
                mp[s[r]] += 1 
            while k < (r - l + 1) - max(mp.values()):
                
                mp[s[l]] -= 1
                l += 1
            maxR = max(maxR, r - l + 1)
        return maxR
                

            

                



