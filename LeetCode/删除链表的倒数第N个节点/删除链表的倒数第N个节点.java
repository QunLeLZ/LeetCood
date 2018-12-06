/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode first = new ListNode(0);
        ListNode second = head;
        ListNode third = head;
        first.next = head;
        for(int i = 1;i < n;i++)
            third = third.next;
        while(third.next != null){
            first = first.next;
            second = second.next;
            third = third.next;
        }
        first.next = second.next;
        if(second == head)
            return head.next;
        return head;
    }
}