/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        
        if(head != null)
        {
            ListNode pre = head;
            ListNode current = head;
            ListNode nextNode = current.next;
            current.next = null;
            while(nextNode != null){
                pre = current;
                current = nextNode;
                nextNode = current.next;
                current.next = pre;
            }
            head = current;
        }
        
        return head;
    }
}