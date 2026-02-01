// Two Sum

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

#include <vector>
#include <unordered_map>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> map;

        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            int complement = target - num;

            if (map.find(complement) != map.end()) {
                return {map[complement], i};
            }
            map[num] = i;
        }
        return {};
    }
};

int main() {
    Solution solution;
    vector<int> nums = {2, 8, 7, 15};
    int target = 9;
    vector<int> result = solution.twoSum(nums, target);

    cout << "Indices: [" << result[0] << ", " << result[1] << "]" << endl;
    return 0;
}