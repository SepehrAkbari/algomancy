// LEETCODE 1 (Easy)

// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
// You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.


/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    typedef struct {
        int key;
        int value;
    } HashMap;

    HashMap* map = (HashMap*)malloc(numsSize * sizeof(HashMap));
    int mapSize = 0;

    for (int i = 0; i < numsSize; i++) {
        int num = nums[i];
        int complement = target - num;

        for (int j = 0; j < mapSize; j++) {
            if (map[j].key == complement) {
                int* out = (int*)malloc(2 * sizeof(int));
                out[0] = map[j].value;
                out[1] = i;    
                *returnSize = 2;
                free(map);
                return out;
            }
        }

        map[mapSize].key = num;
        map[mapSize].value = i;
        mapSize++;
    }
    
    free(map);
    return 0;
}

int main() {
    int nums[] = {2, 8, 7, 11, 15};
    int target = 9;
    int returnSize;
    int* result = twoSum(nums, 5, target, &returnSize);
    free(result);
    return 0;
}