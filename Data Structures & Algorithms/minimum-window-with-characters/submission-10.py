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
        bestr = 0
        bestl = 0
        have = 0
        
        

        while l <= r and r < len(s):
            c = s[r]
            if c in mt:
                mw[c] = mw.get(c, 0) + 1
                if mw[c] == mt[c]:
                    have += 1

            while need == have:
                length = r - l
                if min(best,length) == length:
                    bestl = l
                    bestr = r
                    best = length

                if s[l] in mt:
                    mw[s[l]] = mw[s[l]] - 1
                    if mw[s[l]] < mt[s[l]]:
                        have -= 1
                l += 1

            r += 1
            

        if best == float('inf'):
            return ""
        return s[bestl:bestr+1]
            


                


            

            

            
        
        




        

