// Counting Bits

// Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

package leetcode;

class CountingBits {
    public int[] countBits(int n) {
        int[] result = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            String binary = Integer.toBinaryString(i);
            int ones = 0;
            for (char c : binary.toCharArray()) {
                if (c == '1') {
                    ones++;
                    result[i] = ones;
                }
            }
        }
        return result;
    }

    public static void main(String[] args) {
        CountingBits sol = new CountingBits();
        int n = 5;
        int[] result = sol.countBits(n);
        for (int count : result) {
            System.out.print(count + " ");
        }
        System.out.println();
    }
}