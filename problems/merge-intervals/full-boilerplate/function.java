import java.util.*;

##USER_CODE##

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        List<int[]> _intervalslist = new ArrayList<>();
        while (sc.hasNextLine()) {
            String _row = sc.nextLine().trim();
            if (_row.isEmpty()) break;
            _intervalslist.add(Arrays.stream(_row.split("\\s+")).mapToInt(Integer::parseInt).toArray());
        }
        int[][] intervals = _intervalslist.toArray(new int[0][]);
        int[][] result = new Solution().merge(intervals);
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
