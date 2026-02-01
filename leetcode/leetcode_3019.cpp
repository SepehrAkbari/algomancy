// Number of Key Changes in a Typed String

// You are given a 0-indexed string s typed by a user. Changing a key is defined as using a key different from the last used key. For example, s = "ab" has a change of a key while s = "bBBb" does not have any.

// Return the number of times the user had to change the key.

// Note: Modifiers like shift or caps lock won't be counted in changing the key that is if a user typed the letter 'a' and then the letter 'A' then it will not be considered as a changing of key.

#include <string>
#include <iostream>
using namespace std;

class Solution {
public:
    int countKeyChanges(string s) {
        if (s.empty()) {
            return 0;
        }

        for (char &c : s) {
            c = tolower(c);
        }

        int count = 0;
        for (int i = 0; i < s.size() - 1; ++i) {
            if (s[i] != s[i + 1]) {
                ++count;
            }
        }
        return count;
    }
};

int main() {
    Solution sol;
    string s = "aAaBbB";
    cout << sol.countKeyChanges(s) << endl;
}