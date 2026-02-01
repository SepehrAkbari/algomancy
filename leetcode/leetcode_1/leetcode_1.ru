# Two Sum

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    map = {}
    
    for i in 0...nums.length
        num = nums[i]
        complement = target - num
        if map.key?(complement)
            return [map[complement], i]
        end
        map[num] = i
    end
    []
end

if __FILE__ == $0
    puts two_sum([2,8,7,15], 9).inspect
end