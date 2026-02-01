// Largest Rectangle in Histogram

// Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

#include <vector>
#include <stack>
using namespace std;
#include <iostream>

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> bound_left(n, -1);
        vector<int> bound_right(n, n);

        // finding left bounds
        for (int i = 0; i < n; ++i) {
            // find first smaller on left
            int x = i - 1;
            while (x >= 0 && heights[x] >= heights[i]) {
                x = bound_left[x];
            }
            bound_left[i] = x;
        }

        // finding right bounds
        for (int i = n - 2; i >= 0; --i) {
            int x = i + 1;
            while (x < n && heights[x] >= heights[i]) {
                x = bound_right[x];
            }
            bound_right[i] = x;
        }

        // max area based on bounds
        int max_area = 0;
        for (int i = 0; i < n; ++i) {
            int width = bound_right[i] - bound_left[i] - 1;
            int area = heights[i] * width;
            max_area = max(max_area, area);
        }

        return max_area;
    }
};

int main() {
    Solution sol;
    vector<int> histogram = {2, 1, 5, 6, 2, 3};
    cout << "Largest Rectangle Area: " << sol.largestRectangleArea(histogram) << endl;
    return 0;
}