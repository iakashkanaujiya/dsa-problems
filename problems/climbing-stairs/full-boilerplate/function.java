import java.util.*;

##USER_CODE##

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        int t = Integer.parseInt(sc.nextLine().trim());
        while (t-- > 0) {
            int n = Integer.parseInt(sc.nextLine().trim());
            int result = new Solution().climbStairs(n);
            System.out.println(result);
        }
    }
}
