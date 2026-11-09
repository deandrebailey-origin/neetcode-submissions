class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        mt = {}
        mw = {}

        need = 0
        for c in t:
            if mt.get(c, 0) == 0:
                need += 1
            mt[c] = mt.get(c, 0) + 1

        string = ""
        best = float('inf')
        have = 0
        

        while l <= r and r < len(s):
            if s[r] in mt:
                mw[s[r]] = mw.get(s[r], 0) + 1
                if mw[s[r]] == mt[s[r]]:
                    have += 1

            while need == have:
                length = r - l
                if min(best,length) == length:
                    string = s[l:r+1]
                    best = length

                if s[l] in mt:
                    mw[s[l]] = mw[s[l]] - 1
                    if mw[s[l]] < mt[s[l]]:
                        have -= 1
                
                l += 1
            r += 1
            

        
        return string
            


                


            

            

            
        
        




        

