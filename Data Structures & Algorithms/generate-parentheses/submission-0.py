class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        subset = []
        used = [0] * (2*n)

        def dfs(op, cl):

            if len(subset) == 2 * n:
                res.append("".join(subset))
                return

            if (op >= cl + 1):
                subset.append(')')
                dfs(op,cl+1)
                subset.pop()

            if (n >= op + 1):
                subset.append('(')
                dfs(op+1,cl)
                subset.pop()
            
        dfs(0, 0)
        return res
        



