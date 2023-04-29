"""
There is a singly-linked list head and we want to delete a node 
node in it.

You are given the node to be deleted node. You will not be given 
access to the first node of head.

All the values of the linked list are unique, and it is guaranteed 
that the given node node is not the last node in the linked list.

Delete the given node. Note that by deleting the node, we do not 
mean removing it from memory. We mean:

The value of the given node should not exist in the linked list.
The number of nodes in the linked list should decrease by one.
All the values before node should be in the same order.
All the values after node should be in the same order.

Example 1:
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Explanation: You are given the second node with value 5, the 
    linked list should become 4 -> 1 -> 9 after calling your function.

Example 2:
    Input: head = [4,5,1,9], node = 1
    Output: [4,5,9]
    Explanation: You are given the third node with value 1, the linked 
    list should become 4 -> 5 -> 9 after calling your function.

Assumptions:
    We have the node class written for us
    We are not given the list at all, just the node to remove
    The node is not at the end of the list

Psuedocode:
    We are not given the list and we assume the node is not at the end of the list
    so we cannot access the previous node value at all
    This makes me assume that we can only work with the values given by node, 
    which is next (and really all following nodes) and value

    To 'remove' this node (even though we aren't deleting it), I would just make the node 
    reflect the next one, essentially removing the node from the linked list

    To do this I would make:
    node.val equal to next node.val
    node.next equal to next node.next
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # just change the values of the node to reflect the next node
        node.val = node.next.val
        node.next = node.next.next

# SUBMISSION LINK: https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/941773642/