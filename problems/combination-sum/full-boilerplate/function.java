import java.util.*;

##USER_CODE##

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] candidates = Arrays.stream(sc.nextLine().trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
        int target = Integer.parseInt(sc.nextLine().trim());
        int[][] result = new Solution().combinationSum(candidates, target);
        for (int[] _row : result) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < _row.length; i++) {
                if (i > 0) sb.append(" ");
                sb.append(_row[i]);
            }
            System.out.println(sb);
        }
    }
}
