'''
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.
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

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    curr1 = l1
    curr2 = l2
    dummy = ListNode()
    prev = dummy

    while True:
        if (curr1 is None):
            prev.next = curr2
            break
        if (curr2 is None):
            prev.next = curr1
            break

        if (curr1.val <= curr2.val):
            prev.next = curr1
            curr1 = curr1.next
        else:
            prev.next = curr2
            curr2 = curr2.next
        prev = prev.next

    return dummy.next

def main():
    head1 = ListNode(0, ListNode(2, ListNode(7, ListNode(8))))
    head2 = ListNode(-1, ListNode(3, ListNode(10)))
    assert([-1, 0, 2, 3, 7, 8, 10] == mergeTwoLists(head1, head2).asArray())

    head1 = ListNode(0, ListNode(2, ListNode(7, ListNode(8))))
    head2 = ListNode(1, ListNode(10, ListNode(12, ListNode(100, ListNode(200)))))
    assert([0, 1, 2, 7, 8, 10, 12, 100, 200] == mergeTwoLists(head1, head2).asArray())

    head1 = ListNode(1)
    head2 = None
    assert([1] == mergeTwoLists(head1, head2).asArray())

    head1 = None
    head2 = None
    assert(mergeTwoLists(head1, head2) == None)

main()
