class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        # find the row the value must reside in
        low = 0
        high = len(matrix) - 1
        row = None

        while low <= high:
            mid = (high + low) // 2 # find the middle row
            if target > matrix[mid][0] and target > matrix[mid][len(matrix[mid]) - 1]: # if target greater than the row
                low = mid + 1
            elif target < matrix[mid][0]:
                high = mid - 1
            else:
                # we've found our row to search
                row = matrix[mid]
                print(row)
                # binary search the row
                l = 0
                r = len(matrix[mid]) - 1

                while l <= r:
                    m = (l + r) // 2
                    if matrix[mid][m] == target:
                        return True
                    elif matrix[mid][m] < target:
                        l = m + 1
                    else:
                        r = m - 1
                break
        return False




