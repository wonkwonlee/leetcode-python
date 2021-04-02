"""
Design Linked List


# Using return
This is used the same reason as break. 
The return value doesn't matter and you only want to exit the whole function.

def noReturnFunction():
    return

Result: 288 ms
"""


class Node(object):                         # Node class to be used for linked list

    def __init__(self, val):
        self.val = val                      # Value of current node
        self.next = None                    # Pointer to the next node


class MyLinkedList:                         # Initializes the MyLinkedList object

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None                    # Pointer to the head
        self.size = 0                       # head size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. 
        If the index is invalid, return -1.
        """
        if self.head is None or index >= self.size:
            return -1

        curr = self.head                    # Start at head
        for i in range(index):
            curr = curr.next                # Move to index-th node

        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)                    # Initialize a new node
        node.next = self.head               # Point node.next to current head
        self.head = node                    # Point self.head to the new node

        self.size += 1                      # Increase size by 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.head                    # Start at the head
        if curr is None:                    # If head is none, current head is val
            self.head = Node(val)
        else:
            while curr.next is not None:    # Move to the end of the linked list
                curr = curr.next
            curr.next = Node(val)           # Add at the tail

        self.size += 1                      # Increase size by 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if index > self.size:               # If index is out of bound, nothing happens
            return                          # Similar to break

        curr = self.head
        if index == 0:                      # 0-th index is head
            self.addAtHead(val)
        else:
            for i in range(index - 1):      # Move to one before the index-th node
                curr = curr.next
            node = Node(val)                # Initialize a new node with val
            node.next = curr.next           # Point new node.next to curr.next
            curr.next = node                # Point curr.next to new node

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index >= self.size:              # If index is out of bound, nothing happens
            return                          # Similar to break

        curr = self.head
        if index == 0:                      # 0-th index is head
            self.head = curr.next           # The new head is now curr.next
        else:
            for i in range(index - 1):      # Move to one before the index-th node
                curr = curr.next
            curr.next = curr.next.next      # Point curr.next to curr.next.next

        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
