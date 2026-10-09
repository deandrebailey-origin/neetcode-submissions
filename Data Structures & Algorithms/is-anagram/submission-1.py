class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = {}
        mpt = {}

        for c in s:
            mp[c] = 1 + mp.get(c, 0)
        
        for c in t:
            mpt[c] = 1 + mpt.get(c, 0)

        if mp == mpt:
            return True

        return False

        