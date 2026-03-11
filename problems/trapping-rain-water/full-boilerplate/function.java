import java.util.*;

##USER_CODE##

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        int t = Integer.parseInt(sc.nextLine().trim());
        while (t-- > 0) {
            int[] height = Arrays.stream(sc.nextLine().trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
            int result = new Solution().trap(height);
            System.out.println(result);
        }
    }
}
