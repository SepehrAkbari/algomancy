// LEETCODE 1 (Easy)

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();

        for (i, &num) in nums.iter().enumerate() {
            let complement = target - num;
            if let Some(&idx) = map.get(&complement) {
                return vec![idx, i as i32];
            }
            map.insert(num, i as i32);
        }
        vec![]
    }
}

struct Solution;
fn main() {
    let result = Solution::two_sum(vec![2, 8, 7, 15], 9);
    println!("{:?}", result);
}