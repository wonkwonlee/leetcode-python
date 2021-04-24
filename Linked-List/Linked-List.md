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
* It takes *O(N)* time on average to *visit an element by an index*, where N is the length of the linked list.
    + Unlike the array, we cannot access a random element in constant time


## Add Operation - Singly Linked List
To add a new value after a given node prev,

1. Initialize a new node cur with the given value.

<img width="621" alt="add1" src="https://user-images.githubusercontent.com/28593767/112800504-b1fe3880-90aa-11eb-9707-f834caa63aad.png">

2. Link the "next" field of cur to prev's next node next.

<img width="625" alt="add2" src="https://user-images.githubusercontent.com/28593767/112800505-b1fe3880-90aa-11eb-805d-bb8e47996e5c.png">

3. Link the "next" field in prev to cur.

<img width="626" alt="add3" src="https://user-images.githubusercontent.com/28593767/112800508-b296cf00-90aa-11eb-8137-a38a3ab24103.png">

> Inserting a new node into a linked list takes *O(1)* time complexity, which is very efficient.


## Delete Operation - Singly Linked List
To delete an existing node cur from the singly linked list,
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


## Doubly Linked List
<img width="739" alt="dl" src="https://user-images.githubusercontent.com/28593767/112752327-824d2300-900d-11eb-8db2-b13a359807f0.png">


