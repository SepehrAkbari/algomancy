# LEETCODE 67 (Easy)

# Given two binary strings a and b, return their sum as a binary string.

function addBinary(a::String, b::String)::String
    a10 = parse(BigInt, a; base=2)
    b10 = parse(BigInt, b; base=2)
    sum = a10 + b10
    return string(sum; base=2)
end

println(addBinary("1010", "1011"))