'''
Merge K sorted linked lists and return it as a sorted list.
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

def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = merge2Lists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else None

def merge2Lists(l1, l2):
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
    l1 = ListNode(0, ListNode(2, ListNode(4, ListNode(6))))
    l2 = ListNode(1, ListNode(3, ListNode(4, ListNode(5))))
    l3 = ListNode(5, ListNode(7))
    print(mergeKLists([l1, l2, l3]).asArray())

    l1 = ListNode()
    print(mergeKLists([l1]).asArray())

    l1 = ListNode(-1, ListNode(5))
    l2 = ListNode(7, ListNode(10))
    print(mergeKLists([l1, l2]).asArray())

    l1 = ListNode(8, ListNode(11))
    l2 = ListNode(1, ListNode(2))
    l3 = ListNode(3, ListNode(15))
    l4 = ListNode()
    print(mergeKLists([l1, l2, l3, l4]).asArray())


main()