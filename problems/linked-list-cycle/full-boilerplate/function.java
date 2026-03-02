import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}

##USER_CODE##

public class Main {

    static ListNode buildList(int[] vals) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : vals) { cur.next = new ListNode(v); cur = cur.next; }
        return dummy.next;
    }

    static void printList(ListNode head) {
        StringBuilder sb = new StringBuilder();
        boolean first = true;
        while (head != null) {
            if (!first) sb.append(' ');
            sb.append(head.val);
            first = false;
            head = head.next;
        }
        System.out.println(sb);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] _vals0 = Arrays.stream(sc.nextLine().trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
        ListNode head = buildList(_vals0);
        boolean result = new Solution().hasCycle(head);
        System.out.println(result ? "true" : "false");
    }
}
