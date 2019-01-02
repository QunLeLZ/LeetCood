/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if(head == null) return head;
        ListNode p = new ListNode(0);
        ListNode q = new ListNode(0);
        p.next = head;
        q.next = head;
        int count = 0;
        while(q.next != null){
            q = q.next;
            count++;
        }
        q = p;
        count = k % count;
        for(int i = 0;i < count;i++){
            q = q.next;
        }
        while(q.next != null){
            p = p.next;
            q = q.next;
        }
        q.next = head;
        head = p.next;
        p.next = null;
        return head;
    }
}