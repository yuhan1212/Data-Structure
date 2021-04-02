"""
Data Structure Note in Python
1. Linked List


* Definition for Linked List:

    - A linked list is a sequence of data elements,
      which are connected together via links.
    - Each data element contains a connection to
      another data element in form of a pointer.
    - Python does not have linked lists in its standard library.
    - We implement the concept of linked lists using the concept of nodes.

* Complexity:

    - Visit element takes O(N) time (list takes O(1) as there is index for sequence)
    - Insertion and Deletion take O(1) time
"""

# Node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# print linked list
def print_linked_list(head: Node):
    if not head:
        return ''
    result = ''
    while head:
        result += str(head.val) + ' - '
        head = head.next
    print(result[:-2])


# reversion of linked list
def reverse_linked_list(head: Node) -> Node:
    prev = None
    while head:
        current = head.next
        head.next = prev
        prev = head
        head = current
    return prev


# reversion specific range
def reverse_m_to_n(head: Node, m: int, n: int) -> Node:
    if m == n:
        return head
    dummy = Node(-1)
    dummy.next = head
    pre_m = dummy
    for i in range(m - 1):
        pre_m = pre_m.next
    m_node = pos_m = pre_m.next
    prev = None
    for i in range(n - m + 1):
        current = m_node.next
        m_node.next = prev
        prev = m_node
        m_node = current
    pre_m.next = prev
    pos_m.next = current
    return dummy.next


# insertion of linked list
def insert_to_next_linked_list(head: Node, v: int) -> Node:
    if not head:
        return Node(v)
    temp = head.next
    head.next = Node(v)
    head.next.next = temp
    return head


# merge two sorted linked list
def merge_sorted_linked_list(l1: Node, l2: Node) -> Node:
    if not l1 or not l2:
        return l1 or l2
    dummy = Node(0)
    pd = dummy
    while l1 and l2:
        if l1.val < l2.val:
            pd.next = l1
            l1 = l1.next
        else:
            pd.next = l2
            l2 = l2.next
        pd = pd.next
    pd.next = l1 or l2
    return dummy.next


# partition linked list
def partition_linked_list(head: Node, x: int) -> Node:
    smaller_dummy = Node(0)
    bigger_dummy = Node(0)
    sp = smaller_dummy
    bp = bigger_dummy
    while head:
        if head.val < x:
            sp.next = head
            sp = head
        else:
            bp.next = head
            bp = head
        head = head.next
    bp.next = None
    sp.next = bigger_dummy.next
    return smaller_dummy.next


# remove Nth node from the end
def remove_Nth_node_from_end(head: Node, n: int) -> Node:
    if not head or n < 1:
        return None
    dummy = Node(-1)
    dummy.next = head
    front = dummy
    back = dummy
    while back and n:
        if back:
            back = back.next
            n -= 1
    if n > 0:
        return head
    while back and back.next:
        front = front.next
        back = back.next
    front.next = front.next.next
    return dummy.next


# remove duplicates
def remove_duplicates(head: Node) -> Node:
    if not head:
        return
    pointer = head
    while pointer and pointer.next:
        if pointer.val == pointer.next.val:
            pointer.next = pointer.next.next
        else:
            pointer = pointer.next
    return head


# remove duplicates keep those unique
def remain_unique(head: Node) -> Node:
    if not head:
        return
    dummy = Node(0)
    pointer = dummy
    if head.val != head.next.val:
        pointer.next = head
        pointer = pointer.next
    while head and head.next and head.next.next:
        if head.val != head.next.val != head.next.next.val:
            pointer.next = head.next
            pointer = pointer.next
        head = head.next
    if head.val == head.next.val:
        pointer.next = None
    else:
        pointer.next = head.next
    return dummy.next


'''
# remove duplicates keep those unique
def remain_unique(head: Node) -> Node:
    if not head:
        return
    dummy = Node(-1)
    dummy.next = head
    pointer = dummy
    count = 1
    while head and head.next:
        if head.val == head.next.val:
            count += 1
        elif count > 1:
            count = 1
        else:
            pointer.next = head
            pointer = pointer.next
        head = head.next
    if count == 1:
        pointer.next = head
    else:
        pointer.next = None
    return dummy.next
'''

head3 = Node(1)
head3.next = Node(2)
head3.next.next = Node(3)
head3.next.next.next = Node(4)
head3.next.next.next.next = Node(5)
head3.next.next.next.next.next = Node(6)
head3.next.next.next.next.next.next = Node(7)
print_linked_list(head3)
# 1 - 2 - 3 - 4 - 5 - 6 - 7
print_linked_list(remove_Nth_node_from_end(head3, 3))
# 1 - 2 - 3 - 4 - 6 - 7


'''
head3 = Node(1)
head3.next = Node(3)
head3.next.next = Node(5)
head3.next.next.next = Node(7)
head3.next.next.next.next = Node(2)
head3.next.next.next.next.next = Node(4)
head3.next.next.next.next.next.next = Node(0)
print_linked_list(head3)
# 1 - 3 - 5 - 7 - 2 - 4 - 0
print_linked_list(partition_linked_list(head3, 3))
# 1 - 2 - 0 - 3 - 5 - 7 - 4

head1 = Node(1)
head1.next = Node(5)
head1.next.next = Node(7)
head2 = Node(2)
head2.next = Node(4)
head2.next.next = Node(6)
head2.next.next.next = Node(9)
print_linked_list(merge_sorted_linked_list(head1, head2))
head4 = Node(1)
head4.next = Node(5)
head4.next.next = Node(7)
head3 = None
print_linked_list(merge_sorted_linked_list(head4, head3))

head3 = Node(1)
head3.next = Node(2)
head3.next.next = Node(3)
head3.next.next.next = Node(4)
head3.next.next.next.next = Node(5)
head3.next.next.next.next.next = Node(6)
head3.next.next.next.next.next.next = Node(7)
print_linked_list(head3)
# 1 - 2 - 3 - 4 - 5 - 6 - 7
print_linked_list(reverse_m_to_n(head3, 3, 7))
# 1 - 2 - 5 - 4 - 3 - 6 - 7

# Construct a linked list
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

print_linked_list(head)
# 1 - 2 - 3

head = reverse_linked_list(head)
print_linked_list(head)
# 3 - 2 - 1

head = insert_to_next_linked_list(head, 4)
print_linked_list(head)
# 3 - 4 - 2 - 1

head2 = Node(1)
head2.next = Node(1)
head2.next.next = Node(2)
head2.next.next.next = Node(3)
head2.next.next.next.next = Node(3)
print_linked_list(head2)
# 1 - 1 - 2 - 3 - 3
print_linked_list(remove_duplicates(head2))
# 1 - 2 - 3

head3 = Node(1)
head3.next = Node(1)
head3.next.next = Node(2)
head3.next.next.next = Node(3)
head3.next.next.next.next = Node(3)
head3.next.next.next.next.next = Node(4)
head3.next.next.next.next.next.next = Node(4)
print_linked_list(head3)
# 1 - 1 - 2 - 3 - 3 - 4 - 4
print_linked_list(remain_unique(head3))
# 2
'''

