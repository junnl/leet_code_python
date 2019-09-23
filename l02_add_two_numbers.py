class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    p = 0
    result = t = ListNode(0)

    while (l1 or l2 or p > 0):
        a = l1.val if l1 != None else 0
        b = l2.val if l2 != None else 0

        t.next = ListNode((a + b + p) % 10)
        t = t.next

        l1, l2, p = l1.next if l1 else None, l2.next if l2 else None, (a + b + p) // 10

    return result.next


if __name__ == '__main__':
    add_two_numbers()


