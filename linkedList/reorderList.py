'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
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


def reorderList(head):
    """
    :type head: ListNode
    :rtype: None Do not return anything, modify head in-place instead.
    """
    if (not head or not head.next):
        return
    l1, slow, fast = head, head, head
    prev = None
    while (fast and fast.next):
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = None
    reversedList = reverse(slow)
    merge(head, reversedList)


def reverse(head):
    prev = None
    curr = head
    while (curr):
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev


def merge(l1, l2):
    while (l1):
        l1Next = l1.next
        l2Next = l2.next
        l1.next = l2
        if (l1Next == None):
            break
        l2.next = l1Next
        l1 = l1Next
        l2 = l2Next


def main():
    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    reorderList(l1)
    assert (l1.asArray() == [1, 4, 2, 3])

    l2 = ListNode(1, ListNode(2))
    reorderList(l2)
    assert (l2.asArray() == [1, 2])

    l3 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    reorderList(l3)
    assert (l3.asArray() == [1, 5, 2, 4, 3])


main()
