# Given the head of a singly linked list, reverse it in-place.

def reverse(head):
    prev, current = None, head
    while current is not None:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp
    return prev