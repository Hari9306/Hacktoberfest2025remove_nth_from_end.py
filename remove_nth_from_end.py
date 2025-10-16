class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = second = head  # ❌ Both start from head, should start first from dummy

    for _ in range(n):
        first = first.next

    while first.next:  # ❌ Fails if n == length of list
        first = first.next
        second = second.next

    second.next = second.next.next
    return dummy.next


def print_list(head):
    while head:
        print(head.data, end=" → ")
        head = head.next
    print("None")


# Example
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

print_list(remove_nth_from_end(head, 2))  # Expected 1 → 2 → 3 → 5
