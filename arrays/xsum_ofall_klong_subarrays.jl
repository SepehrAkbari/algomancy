"""
LEETCODE 3318

You are given an array nums of n integers and two integers k and x.
The x-sum of an array is calculated by the following procedure:
Count the occurrences of all elements in the array.
Keep only the occurrences of the top x most frequent elements. If two elements have the same number of occurrences, the element with the bigger value is considered more frequent.
Calculate the sum of the resulting array.
Note that if an array has less than x distinct elements, its x-sum is the sum of the array.
Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i + k - 1].
"""

using DataStructures

function findXSum(nums::Vector{Int}, k::Int, x::Int)::Vector{Int}
    answer = Int[]
    freq_map = Dict{Int, Int}()
    
    for i in 1:k
        freq_map[nums[i]] = get(freq_map, nums[i], 0) + 1
    end
    
    function x_sum(freq_map::Dict{Int, Int})::Int
        max_heap = BinaryMaxHeap{Tuple{Int, Int}}()
        for (num, freq) in freq_map
            push!(max_heap, (freq, num))
        end
        
        x_sum = 0
        for _ in 1:min(x, length(max_heap))
            (freq, num) = pop!(max_heap)
            x_sum += freq * num
        end
        
        return x_sum
    end
    
    push!(answer, x_sum(freq_map))
    for i in k+1:length(nums)
        freq_map[nums[i - k]] -= 1
        if freq_map[nums[i - k]] == 0
            delete!(freq_map, nums[i - k])
        end
        freq_map[nums[i]] = get(freq_map, nums[i], 0) + 1
        
        push!(answer, x_sum(freq_map))
    end
    return answer
end

nums = [1, 1, 2, 2, 3, 4, 2, 3]
k = 6
x = 2

println(findXSum(nums, k, x))