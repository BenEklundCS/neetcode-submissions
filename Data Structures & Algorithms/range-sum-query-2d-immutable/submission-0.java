class NumMatrix {
    private int[][] prefixSumMatrix;

    public NumMatrix(int[][] matrix) {
        int ROWS = matrix.length;
        int COLS = matrix[0].length;

        this.prefixSumMatrix = new int[ROWS + 1][COLS + 1];

        for (int i = 0; i < ROWS; i++) {
            int prefix = 0;
            for (int j = 0; j < COLS; j++) {
                prefix += matrix[i][j];
                int above = prefixSumMatrix[i][j + 1];
                prefixSumMatrix[i + 1][j + 1] = prefix + above;
            }
        }
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        row1++; col1++; row2++; col2++;
        int bottomRight = prefixSumMatrix[row2][col2];
        int above = prefixSumMatrix[row1 - 1][col2];
        int left = prefixSumMatrix[row2][col1 - 1];
        int topLeft = prefixSumMatrix[row1 - 1][col1 - 1];
        return bottomRight - above - left + topLeft;
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */