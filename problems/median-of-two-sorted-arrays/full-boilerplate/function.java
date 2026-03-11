import java.util.*;

##USER_CODE##

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        int t = Integer.parseInt(sc.nextLine().trim());
        while (t-- > 0) {
            int[] nums1 = Arrays.stream(sc.nextLine().trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            int[] nums2 = Arrays.stream(sc.nextLine().trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            double result = new Solution().findMedianSortedArrays(nums1, nums2);
            System.out.println(result);
        }
    }
}
