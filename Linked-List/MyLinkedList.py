"""
Design Linked List
"""
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.next = None
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. 
        If the index is invalid, return -1.
        """
        if not self.index(index):
            return -1
        else:    
            return self.index(index)
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        head.val = val
        head.next = self.val
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        self.next = val
        self.next.next = None

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if self.index(index) <= len(self):
            self.next = val
            self.index


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)