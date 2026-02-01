# 3Sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

function threeSum(nums::Vector{Int})::Vector{Vector{Int}}
    if length(nums) < 3
        return Vector{Vector{Int}}()
    end
    if all(num -> num == 0, nums)
        return [[0, 0, 0]]
    end
    
    sort!(nums)
    res = Set{Vector{Int}}()

    for i in 1:length(nums)
        target = 0 - nums[i]

        map = Dict{Int, Int}()
        for j in (i+1):length(nums)
            complement = target - nums[j]
            if haskey(map, complement)
                sol = sort!([nums[i], nums[j], complement])
                push!(res, sol)
            end
            map[nums[j]] = j
        end
    end
    return collect(res)
end

nums = [-1,0,1,2,-1,-4]
println(threeSum(nums))