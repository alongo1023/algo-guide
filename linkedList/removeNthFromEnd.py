'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def asArray(self):
        head = self
        res = []
        while (head):
            res.append(head.val)
            head = head.next
        return res


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    dummy = ListNode(0, head)
    curr = dummy
    fast = head
    moves = 0
    while (fast and moves < n):
        fast = fast.next
        moves += 1

    while (fast):
        fast = fast.next
        curr = curr.next

    if (curr.next):
        curr.next = curr.next.next

    return dummy.next


def main():
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    assert (removeNthFromEnd(l1, 2).asArray() == [1, 2, 3, 5])

    l2 = ListNode(1, ListNode(4, ListNode(6, ListNode(7))))
    assert (removeNthFromEnd(l2, 5).asArray() == [4, 6, 7])

    l3 = ListNode(1, ListNode(2))
    assert (removeNthFromEnd(l3, 2).asArray() == [2])

    l4 = ListNode(1)
    assert (removeNthFromEnd(l4, 1) is None)


main()
