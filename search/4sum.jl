# LEETCODE 18 (Medium)

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

function fourSum(nums::Vector{Int}, target::Int)::Vector{Vector{Int}}
    if length(nums) < 4
        return Vector{Vector{Int}}()
    end
    
    sort!(nums)
    res = []

    for i in 1:(length(nums) - 3)
        for j in (i + 1):(length(nums) - 2)
            left = j + 1
            right = length(nums)
            while left < right
                sum = nums[i] + nums[j] + nums[left] + nums[right]
                if sum == target
                    push!(res, [nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right && nums[left] == nums[left - 1]
                        left += 1
                    end
                    while left < right && nums[right] == nums[right + 1]
                        right -= 1
                    end
                elseif sum < target
                    left += 1
                else
                    right -= 1
                end
            end
        end
    end
    return collect(res)
end

nums = [1,0,-1,0,-2,2]
target = 1
println(fourSum(nums, target))