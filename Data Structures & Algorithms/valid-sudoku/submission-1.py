class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [set() for _ in range(9)]
        col_check = [set() for _ in range(9)]
        sq_check = [set() for _ in range(9)]
        for row in range(9):
            for col in range(9):
                sq = self.getSudokuSquare(row, col)     # Fetch square index
                if board[row][col] == '.':
                    continue
                # Check redundancy
                elif (board[row][col] in row_check[row]) or (board[row][col] in col_check[col]) or (board[row][col] in sq_check[sq]):
                    return False
                row_check[row].add(board[row][col])
                col_check[col].add(board[row][col])
                sq_check[sq].add(board[row][col])

        return True

    
    def getSudokuSquare(self, row, col):
        """
            This method fetches the square index on a sudoku board using
            row and column indices of an entry.
            The square index follows the pattern: [0, 1, 2,
                                                   3, 4, 5,
                                                   6, 7, 8]

            @param row                  [int] Row index
            @param col                  [int] Column index

            @returnValue sq             [int] Square index
        """

        sq = 0
        if row // 3 == 0:
            sq = (row // 3) + (col // 3)
        else:
            sq = (row // 3) + (col // 3) + (2 ** (row // 3))
        
        return sq