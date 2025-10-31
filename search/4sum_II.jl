# LEETCODE 454 (Medium)

# Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:
# 0 <= i, j, k, l < n
# nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

function fourSumII(nums1::Vector{Int}, nums2::Vector{Int}, nums3::Vector{Int}, nums4::Vector{Int})::Int
    map = Dict{Int, Int}()

    for n1 in nums1
        for n2 in nums2
            if haskey(map, n1 + n2)
                map[n1 + n2] += 1
            else
                map[n1 + n2] = 1
            end
        end
    end

    count = 0
    for n3 in nums3
        for n4 in nums4
            complement = 0 - (n3 + n4)
            if haskey(map, complement)
                count += map[complement]
            end
        end 
    end
    return count
end

nums1 = [1,2]
nums2 = [-2,-1]
nums3 = [-1,2]
nums4 = [0,2]
println(fourSumII(nums1, nums2, nums3, nums4))