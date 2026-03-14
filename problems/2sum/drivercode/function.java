import java.util.*;
import java.io.*;

##USER_CODE##

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        int t = Integer.parseInt(sc.nextLine().trim());
        while (t-- > 0) {
            String _nums_line = sc.nextLine().trim();
            int[] nums = _nums_line.isEmpty() ? new int[0] : Arrays.stream(_nums_line.split("\\s+")).mapToInt(Integer::parseInt).toArray();
            int target = Integer.parseInt(sc.nextLine().trim());
            Solution sol = new Solution();
            int[] result = sol.twoSum(nums, target);
            for(int i=0; i<result.length; i++) {
                if(i > 0) System.out.print(" ");
                System.out.print(result[i]);
            }
            System.out.println();
        }
    }
}
