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
                # Check if row value already present in row hashmap
                if board[row][col] not in rows[row] or board[row][col] == '.':
                    rows[row][board[row][col]] = 1
                else:
                    return False

                # Check if col value already present in col hashmap
                if board[row][col] not in cols[col] or board[row][col] == '.':
                    cols[col][board[row][col]] = 1
                else:
                    return False

                # Check if square value already present in square hashmap
                current_row = row // 3
                current_col = col // 3
                idx_of_square = current_row * 3 + current_col

                if board[row][col] not in squares[idx_of_square] or board[row][col] == '.':
                    squares[idx_of_square][board[row][col]] = 1
                else:
                    return False

        return True

        