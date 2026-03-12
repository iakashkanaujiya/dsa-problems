import java.util.*;

##USER_CODE##

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine())
            return;
        int t = Integer.parseInt(sc.nextLine().trim());
        while (t-- > 0) {
            int[] nums = Arrays.stream(sc.nextLine().trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            int target = Integer.parseInt(sc.nextLine().trim());
            int[] result = new Solution().twoSum(nums, target);
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < result.length; i++) {
                if (i > 0)
                    sb.append(" ");
                sb.append(result[i]);
            }
            System.out.println(sb);
        }
    }
}
