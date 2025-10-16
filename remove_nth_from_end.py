class Node:
    def _init_(self, data):
        self.data = data
        self.next = None


def remove_nth_from_end(head, n):
    dummy = Node(0)
    dummy.next = head
    first = second = dummy  # ✅ Both start from dummy

    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        if first:
            first = first.next

    while first:
        first = first.next
        second = second.next

    # ✅ Safely remove target node
    second.next = second.next.next if second.next else None
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

print_list(remove_nth_from_end(head, 2))
