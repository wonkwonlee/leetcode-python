# Linked List
* Similar to the array, the linked list is also a **linear** data structure.
* Each element in the linked list is actually a separate object while all the objects are **linked together by the reference field** in each element.
* There are two types of linked list: singly-linked list and doubly-linked list.


## Singly Linked List
<img width="530" alt="sl" src="https://user-images.githubusercontent.com/28593767/112752326-80835f80-900d-11eb-98cd-e7afedd359ca.png">

* Each node in a singly-linked list contains not only the value but also *a reference field to link to the next node*. 
    + By this way, the singly-linked list organizes all the nodes in a sequence.
* In most cases, we use **head node** (the first node) to represent the whole list.
* To access the i-th element, we have to traverse from the head node one by one.
    + In the example above, the head is the node 23. 
    + The only way to visit the 3rd node is to use the "next" field of the head node, and then use the "next" field of the second node.
* It takes *O(N)* time on average to *visit an element by index*, where N is the length of the linked list.
    + Unlike the array, we cannot access a random element in constant time


## Doubly Linked List
<img width="739" alt="dl" src="https://user-images.githubusercontent.com/28593767/112752327-824d2300-900d-11eb-8db2-b13a359807f0.png">