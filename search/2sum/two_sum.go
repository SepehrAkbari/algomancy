// LEETCODE 1 (Easy)

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.

import "fmt"

func twoSum(nums []int, target int) []int {
	hashmap := make(map[int]int)

	for i, num := range nums {
		complement := target - num
		if val, ok := hashmap[complement]; ok {
			return []int{val, i}
		}
		hashmap[num] = i
	}
	return nil
}

func main() {
	result := twoSum([]int{2, 8, 7, 15}, 9)
	fmt.Println(result)
}