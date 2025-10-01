# Corrected code
from typing import Optional

class Node:
    def __init__(self, value, successor=None):
        self.value = value
        self.successor = successor

def reverse_linked_list(head: Optional[Node]) -> Optional[Node]:
    """Given the head of a singly linked list, reverse the list, and return the reversed list.
    """
    prev = None
    current = head
    while(current is not None):
        next = current.successor
        current.successor = prev
        prev = current
        current = next
    return prev


"""
Driver to test reverse linked list
"""
def main():
    # Case 1: 5-node list input
    # Expected Output: 1 2 3 4 5
    node1 = Node(1)
    node2 = Node(2, node1)
    node3 = Node(3, node2)
    node4 = Node(4, node3)
    node5 = Node(5, node4)

    result = reverse_linked_list(node5)

    if result == node5:
        print("Reversed!", end=" ")
    else:
        print("Not Reversed!", end=" ")
    while result:
        print(result.value, end=" ")
        result = result.successor
    print()
 
    # Case 2: 1-node list input
    # Expected Output: 0
    node = Node(0)
    result = reverse_linked_list(node)

    if result == node:
        print("Reversed!", end=" ")
    else:
        print("Not Reversed!", end=" ")
    while result:
        print(result.value, end=" ")
        result = result.successor
    print()

    # Case 3: None input
    # Expected Output: None
    result = reverse_linked_list(None)
    if result == None:
        print("Reversed!", end=" ")
    else:
        print("Not Reversed!", end=" ")

    while result:
        print(result.value)
        result = result.successor
    print()

if __name__ == "__main__":
    main()