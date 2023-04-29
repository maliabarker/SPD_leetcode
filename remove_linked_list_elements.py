"""
Given the head of a linked list and an integer val, remove 
all the nodes of the linked list that has Node.val == val, 
and return the new head.

Example 1:
    Input: head = [1,2,6,3,4,5,6], val = 6
    Output: [1,2,3,4,5]
Example 2:
    Input: head = [], val = 1
    Output: []
Example 3:
    Input: head = [7,7,7,7], val = 7
    Output: []

Assumptions
    We assume that val is an integer
    Val may or may not exist
    We need to remove ALL occurences of val

Psuedocode
    Instantiate values for previous node (None) and current node (Head)
    Traverse through the list using the current node as the pointer
        if the current node.val == val to remove
            if the current node is the head node (previous node == None)
                make the new head equal current node.next
            else
                make the previous node.next equal to current node.next to 'skip' current node
        else
            make previous node equal to current node
            *we only do this if the current node is not deleted because if the current node is 
            deleted, the previous node will stay the same
        move forward by making the current node equal to current node.next

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        # start at the head node
        previous_node = None
        current_node = head
        while current_node is not None:
            # if the value of the current node is the one to remove, 
            if current_node.val == val:
                if previous_node is None:
                    # this is head node, just make head equal to next node
                    head = current_node.next
                else:
                    previous_node.next = current_node.next
            else:
                # move onto the next node
                previous_node = current_node
            current_node = current_node.next
        return head

# SOLUTION LINK: https://leetcode.com/problems/remove-linked-list-elements/submissions/941771667/