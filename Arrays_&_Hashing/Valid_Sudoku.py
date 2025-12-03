class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        for row in board:
            list = []
            for num in row:
                if num in list and num != ".":
                    return False
                elif num != ".":
                    list.append(num)

        # check columns

        colDict = {}
        num_rows = len(board)
        num_cols = len(board[0])
        for j in range(num_cols):
            colDict[j] = []
            for i in range(num_rows):
                if board[i][j] != "." and board[i][j] in colDict.get(j):
                    return False
                else:
                    colDict[j].append(board[i][j])

        # check 3X3
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    elif board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
        return True