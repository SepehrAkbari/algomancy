// An array of size N has M different integers. Write a method to create a histogram of the array. Return two arrays, one containing the different integers and the other containing the counts of each integer.

package misc;
import java.util.HashMap;
import java.util.Map;

class CountHistogram {
    public static int[][] make_hist_inefficient(int[] arr) {
        int n = arr.length;
        int[] unique = new int[n];
        int uniqueCount = 0;

        for (int i = 0; i < n; i++) {
            boolean found = false;
            for (int j = 0; j < uniqueCount; j++) {
                if (arr[i] == unique[j]) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                unique[uniqueCount] = arr[i];
                uniqueCount++;
            }
        }

        int[] counts = new int[uniqueCount];
        for (int i = 0; i < uniqueCount; i++) {
            for (int j = 0; j < n; j++) {
                if (arr[j] == unique[i]) {
                    counts[i]++;
                }
            }
        }

        int[][] result = new int[2][uniqueCount];
        for (int i = 0; i < uniqueCount; i++) {
            result[0][i] = unique[i];
            result[1][i] = counts[i];
        }

        return result;
    }

    public static int[][] make_hist_efficient(int[] arr) {
        int n = arr.length;
        Map<Integer, Integer> countMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            countMap.put(arr[i], countMap.getOrDefault(arr[i], 0) + 1);
        }

        int m = countMap.size();

        int[] unique = new int[m];
        int[] counts = new int[m];

        int index = 0;

        for (Map.Entry<Integer, Integer> entry : countMap.entrySet()) {
            unique[index] = entry.getKey();
            counts[index] = entry.getValue();
            index++;
        }

        return new int[][]{unique, counts};
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 1, 7, 8, 3, 7, 1, 9, 10, 0, 1};

        int[][] hist1 = make_hist_inefficient(arr);
        int [][] hist2 = make_hist_efficient(arr);

        System.out.println("Hist1:");
        for (int val : hist1[0]) {
            System.out.print(val + " ");
        }
        System.out.println();
        for (int count : hist1[1]) {
            System.out.print(count + " ");
        }
        System.out.println();

        System.out.println("Hist2:");
        for (int val : hist2[0]) {
            System.out.print(val + " ");
        }
        System.out.println();
        for (int count : hist2[1]) {
            System.out.print(count + " ");
        }
        System.out.println();
    }
}