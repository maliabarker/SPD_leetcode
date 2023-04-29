"""
Given the head of a singly linked list, reverse the list, 
and return the reversed list.

Example 1:
    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
Example 2:
    Input: head = [1,2]
    Output: [2,1]

Assumptions
    We assume we are given node class
    We assume that we are not creating a new list
    We assume that we are returning a list

Psuedocode
    We can do this recursively 
    The base case 
        If we reach the last node or the list is empty, so if head is None or 
        next is None, then we return head
    The recursive case
        we make the new head a recursive call to the reverse function and pass in the next node
        make sure the next next node of current head equals head node (which will reverse list)
        make current head.next equal none, making it the new tail node
    return the new head
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
    if head is None or head.next is None:
        return head
    new_head = reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head

# SOLUTION LINK: https://leetcode.com/problems/reverse-linked-list/submissions/941767748/