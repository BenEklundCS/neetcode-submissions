class Solution:
    def isValidSudoku(self, board) -> bool:
        rows = {}
        cols = {}
        squares = {}

        # create dicts for O(1) lookup of seen values
        for i in range(9):
            rows[i] = {}
            cols[i] = {}
            squares[i] = {}

        row_count = 0
        for row in range(len(board)):
            for col in range(len(board[row])):
                value = board[row][col]

                current_row = row // 3
                current_col = col // 3
                idx_of_square = current_row * 3 + current_col

                if value == '.': # skip empty cells
                    continue

                if value in rows[row] or value in cols[col] or value in squares[idx_of_square]:
                    return False
                
                rows[row][value] = 1
                cols[col][value] = 1
                squares[idx_of_square][value] = 1
        return True

        