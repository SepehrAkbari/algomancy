// Broken Calculator

// There is a broken calculator that has the integer startValue on its display initially. In one operation, you can:
// multiply the number on display by 2, or
// subtract 1 from the number on display.
// Given two integers startValue and target, return the minimum number of operations needed to display target on the calculator.

#include <iostream>

class Solution {
public:
    int brokenCalc(int startValue, int target) {
        int count = 0;
        while (target > startValue) {
            count++;
            if (target % 2 == 1) {
                target++;
            } else {
                target /= 2;
            }
        }
        return count + (startValue - target);
    }
};

int main() {
    Solution sol;
    int startValue = 5;
    int target = 8;
    std::cout << "Minimum operations: " << sol.brokenCalc(startValue, target) << std::endl;
    return 0;
}