class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] == '.':
                    continue
                elif board[r][c] in seen:
                    return False
                seen.add(board[r][c])
        sq_beg = [0, 3, 6, 9]
        for square in range(9):
            seen = set()            
            rows = list(range(sq_beg[square % 3], sq_beg[(square % 3) + 1]))
            cols = list(range(sq_beg[(square // 3) % 3], sq_beg[((square // 3) % 3) + 1]))
            for r in rows:
                for c in cols:
                    if board[r][c] == '.':
                        continue
                    elif board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
        return True
