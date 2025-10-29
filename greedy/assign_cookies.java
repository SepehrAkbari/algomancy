// LEETCODE 455 (Easy)

// Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
// Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

import java.util.Arrays;

class assignCookies {
    public int findContentChildren(int[] g, int[] s) {
        Arrays.sort(g);
        Arrays.sort(s);
        
        int child = 0;
        int cookie = 0;

        // until there are no more children or cookies
        while (child < g.length && cookie < s.length) {
            // if the cookie can satisfy the child
            if (s[cookie] >= g[child]) {
                child++;
            }
            cookie++;
        }

        return child;
    }

    public static void main(String[] args) {
        assignCookies solution = new assignCookies();
        int[] g = {1, 2, 3, 4};
        int[] s = {3, 1};
        System.out.println(solution.findContentChildren(g, s));
    }
}