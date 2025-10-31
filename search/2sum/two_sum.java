// LEETCODE 1 (Easy)

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int num = nums[i];
            int complement = target - num;
            if (map.containsKey(complement)) {
                return new int[] { map.get(complement), i };
            }
            map.put(num, i);
        }
        return new int[] {};
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] result = solution.twoSum(new int[] {2, 8, 7, 15}, 9);
        System.out.println("Indices: [" + result[0] + ", " + result[1] + "]");
    }
}