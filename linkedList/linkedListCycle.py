'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index of the
node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
'''

# Definition for singly-linked list.
class ListNode(object):
 def __init__(self, x = 0, next = None):
     self.val = x
     self.next = next

def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    if (not head):
        return False

    slow = head
    fast = head.next
    while (fast and fast.next):
        if (slow == fast.next):
            return True

        slow = slow.next
        fast = fast.next.next

    return False

def main():
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert(not hasCycle(head1))

    head2 = ListNode()
    assert(not hasCycle(head2))

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node1
    assert(hasCycle(node1))


main()
