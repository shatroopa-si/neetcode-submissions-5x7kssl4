class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [set() for _ in range(9)]
        col_check = [set() for _ in range(9)]
        sq_check = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                sq = ((row // 3) * 3) + (col // 3)
                if board[row][col] == '.':
                    continue
                # Check redundancy
                elif (val in row_check[row]) or (val in col_check[col]) or (val in sq_check[sq]):
                    return False
                row_check[row].add(val)
                col_check[col].add(val)
                sq_check[sq].add(val)

        return True