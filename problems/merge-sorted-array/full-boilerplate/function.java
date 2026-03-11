import java.util.*;

##USER_CODE##

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        int t = Integer.parseInt(sc.nextLine().trim());
        while (t-- > 0) {
            int[] nums1 = Arrays.stream(sc.nextLine().trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            int m = Integer.parseInt(sc.nextLine().trim());
            int[] nums2 = Arrays.stream(sc.nextLine().trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            int n = Integer.parseInt(sc.nextLine().trim());
            int[] result = new Solution().merge(nums1, m, nums2, n);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0) sb.append(" ");
                sb.append(result[i]);
            }
            System.out.println(sb);
        }
    }
}
