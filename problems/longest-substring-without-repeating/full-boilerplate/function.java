import java.util.*;

##USER_CODE##

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        if (!sc.hasNextLine()) return;
        int t = Integer.parseInt(sc.nextLine().trim());
        while (t-- > 0) {
            String s = sc.nextLine().trim();
            int result = new Solution().lengthOfLongestSubstring(s);
            System.out.println(result);
        }
    }
}
