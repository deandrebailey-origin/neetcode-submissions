class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,r = 0,0

        best = 0
        best_character = s[l]
        m = {}

        while r < len(s):
            length = r - l + 1
            m[s[r]] = m.get(s[r],0) + 1
            if m[best_character] < m[s[r]]:
                best_character = s[r]
            mismatches = length - m[best_character]
            print(mismatches,length)
            if mismatches > k:
                m[s[l]] -= 1
                l += 1
            length = r - l + 1
            best = max(best, length)
            r += 1

        return best


