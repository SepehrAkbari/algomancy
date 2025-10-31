// LEETCODE 1 (Easy)

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const map = new Map();

    for (let i = 0; i < nums.length; i++) {
        const num = nums[i];
        const complement = target - num;

        if (map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(num, i);
    }
    return [];
};

console.log(twoSum([2, 8, 7, 11, 15], 9));