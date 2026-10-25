class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        v = {}
        answer = False

        def dfs(i,j,l) -> bool:
            if i < 0 or j < 0 or i > len(board) - 1 or j > len(board[0]) - 1 or board[i][j] != word[l] or v.get((i,j)):
                return False
            
            if board[i][j] == word[len(word)-1] and l == len(word)-1:
                return True

            v[(i,j)] = True

            print(board[i][j])

            up = dfs(i+1,j,l+1) 
            down = dfs(i-1,j,l+1) 
            right = dfs(i,j+1,l+1) 
            left = dfs(i,j-1,l+1)

            v[(i,j)] = False

            return up or down or right or left

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    answer = dfs(i,j,0)
                    if answer == True:
                        return True

        return answer



