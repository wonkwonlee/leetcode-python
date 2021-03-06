# Linked List
* Similar to the array, the linked list is also a **linear** data structure.
* Each element in the linked list is actually a separate object while all the objects are **linked together by the reference field** in each element.
* There are two types of linked list: singly linked list and doubly linked list.


## Singly Linked List
<img width="530" alt="sl" src="https://user-images.githubusercontent.com/28593767/112752326-80835f80-900d-11eb-98cd-e7afedd359ca.png">

* Each node in a singly linked list contains not only the value but also *a reference field to link to the next node*. 
    + By this way, the singly linked list organizes all the nodes in a sequence.
* In most cases, we use **head node** (the first node) to represent the whole list.
* To access the i-th element, we have to traverse from the head node one by one.
    + In the example above, the head is the node 23. 
    + The only way to visit the 3rd node is to use the "next" field of the head node, and then use the "next" field of the second node.
* It takes *O(N)* time on average to *visit an element by an index*, where N is the length of the linked list.
    + Unlike the array, we cannot access a random element in constant time

### Design Singly Linked List
1. Initiate a new linked list: represent a linked list using the head node.
```py
def __init__(self):
    """
    Initialize your data structure here.
    """
    self.head = None
    self.size = 0
```
2. Traverse the linked list to get element by index.
```py
def get(self, index: int) -> int:
    """
    Get the value of the index-th node in the linked list. 
    If the index is invalid, return -1.
    """
    if self.head is None or index >= self.size:
        return -1

    curr = self.head
    for i in range(index):
        curr = curr.next

    return curr.val
```
3. Add a new node.
```py
def addAtHead(self, val: int) -> None:
    """
    Add a node of value val before the first element of the linked list. 
    After the insertion, the new node will be the first node of the linked list.
    """
    node = Node(val)
    node.next = self.head
    self.head = node

    self.size += 1

def addAtTail(self, val: int) -> None:
    """
    Append a node of value val to the last element of the linked list.
    """
    curr = self.head
    if curr is None:
        self.head = Node(val)
    else:
        while curr.next is not None:
            curr = curr.next
        curr.next = Node(val)

    self.size += 1

def addAtIndex(self, index: int, val: int) -> None:
    """
    Add a node of value val before the index-th node in the linked list. 
    If index equals to the length of linked list, 
    the node will be appended to the end of linked list. 
    If index is greater than the length, the node will not be inserted.
    """
    if index > self.size:
        return

    curr = self.head
    if index == 0: 
        self.addAtHead(val)
    else:
        for i in range(index - 1):
            curr = curr.next
        node = Node(val)
        node.next = curr.next
        curr.next = node

        self.size += 1
```
4. Delete a node.
```py
def deleteAtIndex(self, index: int) -> None:
    """
    Delete the index-th node in the linked list, if the index is valid.
    """
    if index >= self.size:
        return

    curr = self.head
    if index == 0: 
        self.head = curr.next
    else:
        for i in range(index - 1):
            curr = curr.next
        curr.next = curr.next.next

    self.size -= 1
```


## Add Operation - Singly Linked List
To add a new value after a given node prev,

1. Initialize a new node curr with the given value.

<img width="621" alt="add1" src="https://user-images.githubusercontent.com/28593767/112800504-b1fe3880-90aa-11eb-9707-f834caa63aad.png">

2. Link the "next" field of curr to prev's next node next.

<img width="625" alt="add2" src="https://user-images.githubusercontent.com/28593767/112800505-b1fe3880-90aa-11eb-805d-bb8e47996e5c.png">

3. Link the "next" field in prev to cur.

<img width="626" alt="add3" src="https://user-images.githubusercontent.com/28593767/112800508-b296cf00-90aa-11eb-8137-a38a3ab24103.png">

> Inserting a new node into a linked list takes *O(1)* time complexity, which is very efficient.


## Delete Operation - Singly Linked List
To delete an existing node curr from the singly linked list,

1. Find cur's previous node prev and its next node next.

<img width="756" alt="del1" src="https://user-images.githubusercontent.com/28593767/112800510-b296cf00-90aa-11eb-80bf-fa0159174f83.png">

2. Link prev to cur's next node next.

<img width="759" alt="del2" src="https://user-images.githubusercontent.com/28593767/112800512-b32f6580-90aa-11eb-897a-3a37387c145f.png">

> Deleting a node in a linked list takes *O(N)* time complexity, as we have to traverse from head node to find out prev.


## Two Pointer Technique
1. **Two pointers starts at different position**: one starts at the beginning while another starts at the end
    + Since we can only traverse in one direction, the first scenario might not work for a singly linked list. 
2. **Two pointers are moved at different speed**: one is faster while another one might be slower.
    + The second scenario, which is also called **slow-pointer and fast-pointer technique**, is useful for a singly linked list.

* Two-pointer technique in the linked list is similar to that in an array, but is trickier and error-prone.
    1. **Always examine if the node is null before you call the next field.**
        + Getting the next node of a null node will cause the null-pointer error.
        + For example, before you run fast = fast.next.next, you need to examine both fast and fast.next is not null.
    2. **Carefully define the end conditions of your loop.**
        + Run several examples to make sure your end conditions will not result in an endless loop. 
        + Also take first tip into consideration when you define your end conditions.

### Complexity Analysis
* If you only use pointers without any other extra space, the space complexity will be *O(1)*.
* To calculate the time complexity, we need to analyze *how many times we will run our loop*.
    0. Assume that we move the faster pointer 2 steps each time and move the slower pointer 1 step each time.
    1. If there is no cycle, the fast pointer takes N/2 times to reach the end of the linked list, where N is the length of the linked list.
    2. If there is a cycle, the fast pointer needs M times to catch up the slower pointer, where M is the length of the cycle in the list.
* Then M <= N, and we will run the loop *up to N times*.
* Thus, the time complexity is *O(N)*.


## Reverse Linked List
> One solution to reverse a singly linked list is to *iterate the nodes in original order and move them to the head of the list one by one*.

1. From the original head node, move the next node of the head node to the head of the list.

<img width="493" alt="reverse1" src="https://user-images.githubusercontent.com/28593767/113301269-cd32a780-9339-11eb-82e1-b22856c7009f.png">

2. Then, move the next node of the original head node, to the head of the list.

<img width="493" alt="reverse2" src="https://user-images.githubusercontent.com/28593767/113301273-cefc6b00-9339-11eb-934b-b6ff6ebbf92d.png">

3. If the next node of the original head node is null, stop and return the new head.

<img width="493" alt="reverse3" src="https://user-images.githubusercontent.com/28593767/113301282-cf950180-9339-11eb-94a7-1fa2df273283.png">

* Each node moves exactly once, so the time complexity is *O(N)*, where N is the length of the linked list, and the space complexity is *O(1)*.

```py
def reverseList(self, head: ListNode) -> ListNode:
    # ListNode prev store reversed linked list
    prev = None
    while head:
        # Update new variable next to head.next, and head.next to prev
        next, head.next = head.next, prev
        # Update prev to current head, and head to next(= head.next)
        prev, head = head, next

    return prev
```

### Tips for Linked List Classic Problems
1. Going through some test cases will save you time.
2. Feel free to use several pointers at the same time.
3. In many cases, you need to track the previous node of the current node.


## Doubly Linked List
<img width="739" alt="dl" src="https://user-images.githubusercontent.com/28593767/112752327-824d2300-900d-11eb-8db2-b13a359807f0.png">

* The doubly linked list has "prev" reference field which links to the previous node of the current node.
* The doubly linked list can access data in the same exact way as in a singly linked list.
    1. Not able to access a random position in constant time.
    2. Traverse from the head to get the i-th node.
    3. The time complexity in the worse case will be *O(N)*, where N is the length of the linked list.

### Design Singly Linked List
1. Initiate a new linked list: represent a linked list using the head node.
```py
def __init__(self):
    """
    Initialize your data structure here.
    """
    self.head = None
    self.size = 0
```
2. Traverse the linked list to get element by index.
```py
def get(self, index: int) -> int:
    """
    Get the value of the index-th node in the linked list. 
    If the index is invalid, return -1.
    """
    if self.head is None or index >= self.size:
        return -1

    curr = self.head
    for i in range(index):
        curr = curr.next

    return curr.val
```
3. Add a new node.
```py
def addAtHead(self, val: int) -> None:
    """
    Add a node of value val before the first element of the linked list. 
    After the insertion, the new node will be the first node of the linked list.
    """
    node = Node(val)
    node.next = self.head
    self.head = node
    self.prev = node

    self.size += 1

def addAtTail(self, val: int) -> None:
    """
    Append a node of value val to the last element of the linked list.
    """
    node = Node(val)
    curr = self.head
    if curr is None:
        self.head = node
    else:
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        node.prev = curr

    self.size += 1

def addAtIndex(self, index: int, val: int) -> None:
    """
    Add a node of value val before the index-th node in the linked list. 
    If index equals to the length of linked list, 
    the node will be appended to the end of linked list. 
    If index is greater than the length, the node will not be inserted.
    """
    if index > self.size:
        return

    curr = self.head
    if index == 0: 
        self.addAtHead(val)
    else:
        for i in range(index - 1):
            curr = curr.next
        node = Node(val)
        node.next = curr.next
        curr.next = node
        node.prev = curr

        self.size += 1
```
4. Delete a node.
```py
def deleteAtIndex(self, index: int) -> None:
    """
    Delete the index-th node in the linked list, if the index is valid.
    """
    if index < 0 or index >= self.size:
        return

    curr = self.head
    if index == 0: 
        self.head = curr.next
    else:
        for i in range(index - 1):
            curr = curr.next
        curr.next.prev = curr
        curr.next = curr.next.next

    self.size -= 1
```


## Add Operation - Doubly Linked List
To insert a new node curr after an existing node prev,

1. Link curr with prev and next, where next is the original next node of prev.

<img width="851" alt="add1" src="https://user-images.githubusercontent.com/28593767/120182499-74a05d80-c249-11eb-8bc8-fa59493ec0a2.png">

2. Re-link the prev and next with cur.

<img width="857" alt="add2" src="https://user-images.githubusercontent.com/28593767/120182511-766a2100-c249-11eb-93a5-df6cd1def76d.png">

> Similar to the singly linked list, both the time and the space complexity of the add operation are *O(1)*.


## Delete Operation - Doubly Linked List
To delete an existing node curr from the doubly linked list, 

1. Link its previous node prev with its next node next.
    + Unlike the singly linked list, it is easy to get the previous node in constant time with the "prev" field.

<img width="739" alt="del1" src="https://user-images.githubusercontent.com/28593767/120183159-4bcc9800-c24a-11eb-8f10-8857e2159dfa.png">
<img width="744" alt="del2" src="https://user-images.githubusercontent.com/28593767/120183163-4cfdc500-c24a-11eb-804c-7aafec55a3b2.png">

2. Node 6 is not in the doubly linked list now.

> Since we no longer need to traverse the linked list to get the previous node, both the time and space complexity are *O(1)*.


## Singly Linked List vs Doubly Linked List
* Review the performance of the singly linked list and doubly linked list.
* They are similar in many operations.
    1. Both of them are *not able to access the data at a random position* in constant time.
    2. Both of them are able to *add a new node after given node or at the beginning of the list in O(1) time*.
    3. Both of them are able to *delete the first node in O(1) time*.
* But it is a little different to *delete a given node* (including the last node).
    + In a singly linked list, it is not able to get the previous node of a given node so we have to spend *O(N)* time to find out the previous node before deleting the given node.
    + In a doubly linked list, it will be much easier because we can get the previous node with the "prev" reference field. So we can delete a given node in *O(1)* time.


## Array vs Linked List
<img width="670" alt="table" src="https://user-images.githubusercontent.com/28593767/121190687-41437b80-c8a6-11eb-88db-1bb0333d0232.png">

* If you need to add or delete a node frequently, a linked list could be a good choice.
* If you need to access an element by index often, an array might be a better choice than a linked list.

