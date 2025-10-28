// LEETCODE 70 (Easy)

// You are climbing a staircase. It takes n steps to reach the top.
// Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

#include <stdio.h>

int climbStairs(int n) {
    if (n <= 3){
        return n;
    }

    int f1 = 3, f2 = 2, f = 0;

    for (int i = 3; i < n; i++) {
        f = f1 + f2;
        f2 = f1;
        f1 = f;
    }

    return f;
}

int main() {
    printf("%d\n", climbStairs(5));
    return 0;
}