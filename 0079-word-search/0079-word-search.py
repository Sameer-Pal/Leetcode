class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      r=len(board)
      c=len(board[0])
      def helper(row,col,i):
        if i==len(word):
            return True
        if row < 0 or col < 0 or row >= r or col >= c or board[row][col] != word[i]: return  False
        
        temp=board[row][col]
        board[row][col] = "visited"

        if helper(row+1,col,i+1) or helper(row,col+1,i+1) or helper(row-1,col,i+1) or helper(row,col-1,i+1):
            return True 
    
        board[row][col] = temp
        return False
      for i in range(r):
        for j in range(c):
            if helper(i,j,0):
                return True
      return False