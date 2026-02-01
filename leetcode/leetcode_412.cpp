// Fizz Buzz

// Given an integer n, return a string array answer (1-indexed) where:
// answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
// answer[i] == "Fizz" if i is divisible by 3.
// answer[i] == "Buzz" if i is divisible by 5.
// answer[i] == i (as a string) if none of the above conditions are true.

#include <vector>
#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> answer;

        // from 1 to n
        for (int i = 1; i <= n; ++i) {
            // checking remainder of 0 (divisible)
            if (i % 3 == 0 && i % 5 == 0) {
                // adding to the array
                answer.push_back("FizzBuzz");
            } else if (i % 3 == 0) {
                answer.push_back("Fizz");
            } else if (i % 5 == 0) {
                answer.push_back("Buzz");
            } else {
                // converting the iterator as string
                answer.push_back(to_string(i));
            }
        }
        return answer;
    }
};

int main() {
    Solution sol;
    int n = 15;
    vector<string> result = sol.fizzBuzz(n);
    for (const string& s : result) {
        cout << s << " ";
    }
    cout << endl;
    return 0;
}