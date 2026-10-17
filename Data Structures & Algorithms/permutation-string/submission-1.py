class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        l, r = 0, len(s1) - 1

        s3 = sorted(s1)


        while r <= len(s2):
            s4 = sorted(s2[l:r+1])
            if s4 == s3:
                return True
            l += 1
            r += 1

        return False


            



        