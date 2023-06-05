#Given the head of a singly linked list, return true if it is a palindrome or false otherwise. You can see more about in https://leetcode.com/problems/palindrome-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        values = []
        node = head
        while node:
            values.append(node.val)
            node = node.next
        
        reversed_values = values[::-1]
        return values == reversed_values

node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

solution = Solution()
print(solution.isPalindrome(node1))
