class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                    if board[r][c] == ".":
                            continue
                    # Check Row
                    if board[r][c] in rows[r]:
                            return False
                    rows[r].add(board[r][c])
                    # Check Column
                    if board[r][c] in cols[c]:
                            return False
                    cols[c].add(board[r][c])
                    # Check Squares
                    box_index = (r // 3) * 3 + (c // 3)
                    if board[r][c] in squares[box_index]:
                            return False
                    squares[box_index].add(board[r][c])
        return True