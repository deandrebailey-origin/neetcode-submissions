class Solution:
    def partition(self, s: str) -> List[List[str]]:

        res = []
        subset = []

        #print("".join(subset))
        
        def dfs(i):
            if i>len(s)-1:
                res.append(subset.copy())
                return

            
            for j in range(i+1,len(s)+1):
                string = s[i:j] 
                if string == string[::-1]:
                    subset.append(string)
                    dfs(j)
                    print(subset)
                    subset.pop()

        dfs(0)
        
        return res
