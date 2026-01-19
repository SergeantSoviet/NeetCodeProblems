class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        
        def check(r, c, count):
            if count == len(word):
                return True
            
            if (min(r, c) < 0 or r >= rows or c >= cols or
                word[count] != board[r][c] or board[r][c] == '#'):
                return False

            temp = board[r][c]
            board[r][c] = "#"
            found = (check(r+1, c, count+1) or
            check(r-1, c, count+1) or
            check(r, c+1, count+1) or
            check(r, c-1, count+1))

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if check(r, c , 0):
                    return True
        return False