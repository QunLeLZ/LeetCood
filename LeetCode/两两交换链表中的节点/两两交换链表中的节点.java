/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if(head == null)
            return null;
        if(head.next == null)
            return head;
        ListNode first = new ListNode(0);
        first.next = head;
        ListNode second = head;
        head = head.next;
        while(second != null && second.next != null){
            ListNode tmp = second.next.next;
            second.next.next = second;
            first.next = second.next;
            second.next = tmp;
            first = second;
            second = second.next;
        }
         return head;
    }
}