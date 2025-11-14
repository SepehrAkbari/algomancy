// LEETCODE 202 (Easy)

// Write an algorithm to determine if a number n is happy.
// A happy number is a number defined by the following process:
// Starting with any positive integer, replace the number by the sum of the squares of its digits.
// Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
// Those numbers for which this process ends in 1 are happy.
// Return true if n is a happy number, and false if not.

#include <set>
#include <iostream>
using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        set<int> seen;
        while (n != 1) {
            int sum = 0;
            for (char c : to_string(n)) {
                int digit = c - '0';
                sum += digit * digit;
            }
            n = sum;
            if (seen.count(n)) {
                return false;
            }
            seen.insert(n);
        }
        return true;
    }
};

int main() {
    Solution sol;
    cout << boolalpha << sol.isHappy(19) << endl;
    cout << boolalpha << sol.isHappy(2) << endl;
    return 0;
}