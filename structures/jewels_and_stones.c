// LEETCODE 771

// You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

// Letters are case sensitive, so "a" is considered a different type of stone from "A".

#include <stdio.h>

int numJewelsInStones(char* jewels, char* stones) {
    int count = 0;

    // iterating through each stone
    for (int i = 0; stones[i] != '\0'; i++) {
        // iterating through each jewel
        for (int j = 0; jewels[j] != '\0'; j++) {
            // checking if the stone is a jewel
            if (stones[i] == jewels[j]) {
                count++;
                break;
            }
        }
    }
    return count;
}

int main() {
    printf("%d\n", numJewelsInStones("aA", "aAAbbbb"));
    return 0;
}