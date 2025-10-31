# LEETCODE 1 (Easy)

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

function two_sum(nums::Vector{Int}, target::Int)::Vector{Int}
    map = Dict{Int, Int}()

    for (i, num) in enumerate(nums)
        complement = target - num
        if haskey(map, complement)
            return [map[complement], i]
        end
        map[num] = i
    end
    return []
end

nums = [2, 8, 7, 11, 15]
target = 9
println(two_sum(nums, target))