// Set Matrix Zeroes

// Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
// You must do it in place.

#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty()) {
            return;
        }

        // dimensions of the matrix
        int m = matrix.size();
        int n = matrix[0].size();

        // zeros in rows and columns
        vector<bool> zrows(m, false);
        vector<bool> zcols(n, false);

        // mark zeros in rows and columns
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 0) {
                    zrows[i] = true;
                    zcols[j] = true;
                }
            }
        }

        // set zeros in marked rows
        for (int i = 0; i < m; ++i) {
            if (zrows[i]) {
                for (int j = 0; j < n; ++j) {
                    matrix[i][j] = 0;
                }
            }
        }

        // set zeros in marked columns
        for (int j = 0; j < n; ++j) {
            if (zcols[j]) {
                for (int i = 0; i < m; ++i) {
                    matrix[i][j] = 0;
                }
            }
        }
    }
};

int main() {
    Solution solution;
    vector<vector<int>> matrix = {
        {1, 1, 1},
        {1, 0, 1},
        {1, 1, 1}
    };
    solution.setZeroes(matrix);

    for (const auto& row : matrix) {
        for (const auto& val : row) {
            cout << val << " ";
        }
        cout << endl;
    }
    return 0;
}