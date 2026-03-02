import java.util.*;

##USER_CODE##

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] height = Arrays.stream(sc.nextLine().trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
        int result = new Solution().maxArea(height);
        System.out.println(result);
    }
}
