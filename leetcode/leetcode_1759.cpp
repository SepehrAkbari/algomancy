// Count Homogenous Substrings

// Given a string s, return the number of homogenous substrings of s. Since the answer may be too large, return it modulo 10^9 + 7.
// A string is homogenous if all the characters of the string are the same.
// A substring is a contiguous sequence of characters within a string.

#include <iostream>
#include <string>

class Solution {
public:
    int countHomogenous(std::string s) {
        if (s.empty()){
            return 0;
        }

        const int mod = 1e9 + 7;
        // initialization for first character
        int out = 1;
        int count = 1;

        // iterating through the string
        for(int i = 1, n = s.length(); i < n; i++){
            // if current character is same as previous one
            if (s[i] == s[i - 1]){
                ++count;
            // if different, reset count sinc e new homogenous substring starts
            } else {
                count = 1;
            }
            // add current count to output
            out = (out + count) % mod;
        }
        return out;
    }
};

int main() {
    Solution solution;
    std::cout << solution.countHomogenous("xy") << std::endl;
    return 0;
}