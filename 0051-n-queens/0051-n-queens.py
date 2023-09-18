class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def N_queen(arr, row, col):
            for i in range(row):
                if arr[i][col]:
                    return False

            maxLeft = min(row, col)
            for i in range(1, maxLeft + 1):
                if arr[row - i][col - i]:
                    return False

            maxright = min(row, len(arr) - col - 1)
            for i in range(1, maxright + 1):
                if arr[row - i][col + i]:
                    return False
            return True

        def format_board(arr):
            formatted = []
            for row in arr:
                formatted_row = "".join(["Q" if col else "." for col in row])
                formatted.append(formatted_row)
            return formatted

        def display(arr, row):
            if row == len(arr):
                ans.append(format_board(arr))
                return 1
            for col in range(len(arr)):
                if N_queen(arr, row, col):
                    arr[row][col] = True
                    display(arr, row + 1)
                    arr[row][col] = False
        ans = []
        arr = [[False] * n for _ in range(n)]
        display(arr, 0)
        return ans


