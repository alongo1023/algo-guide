'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
'''


# Definition for singly-linked list.
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


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    curr = head

    while (curr):
        nextTemp = curr.next
        curr.next = prev
        prev = curr
        curr = nextTemp

    return prev


def reverseListViaStack(head):
    """
    :param head: ListNode
    :return: ListNode
    """
    stack = []

    while (head):
        stack.append(head.val)
        head = head.next

    curr = ListNode()
    res = curr
    while (len(stack) > 0):
        curr.next = ListNode(stack.pop())
        curr = curr.next
    return res.next


def main():
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head2 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(reverseList(head1).asArray())
    print(reverseListViaStack(head2).asArray())

    head3 = ListNode(3, ListNode(100))
    head4 = ListNode(3, ListNode(100))
    print(reverseList(head3).asArray())
    print(reverseListViaStack(head4).asArray())

    head5 = ListNode()
    head6 = ListNode()
    print(reverseList(head5).asArray())
    print(reverseListViaStack(head6).asArray())


main()
