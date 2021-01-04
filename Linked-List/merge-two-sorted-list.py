class ListNode:
    def __init__(self, val=0):
        self.next = None
        self.val = val

def mergeListIterative(l1, l2):
    dummy = head = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            head.next = l1
            l1 = l1.next
        else:
            head.next = l2
            l2 = l2.next
        head = head.next

    if l1:
        head.next = l1
    if l2:
        head.next = l2

    return dummy.next

def mergeListRecursive(l1, l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    elif l1.val < l2.val:
        l1.next = mergeListRecursive(l1.next, l2)
        return l1
    else:
        l2.next = mergeListRecursive(l1, l2.next)
        return l2

def printList(l):
    while l:
        print(l.val)
        l = l.next

def constructList():
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    return l1, l2

def main():
    print('Iteratively merge lists:')
    l1, l2 = constructList()
    mergedIterative = mergeListIterative(l1, l2)
    printList(mergedIterative)

    print('Recursively merge lists:')
    l1, l2 = constructList()
    mergedRecursive = mergeListRecursive(l1, l2)
    printList(mergedRecursive)


if __name__ == "__main__":
	main()
