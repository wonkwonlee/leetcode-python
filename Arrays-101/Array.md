# Array
* An Array is a collection of items - The items are stored in contiguous memory locations.
* The two most primitive Array operations are writing elements and reading elements.
* The capacity of an Array can be checked by len(arr)


## Basic Array Operations
* **Insert** a new element into the array.
* **Delete** an element from the existing array.
* **Search** for a particular element in the array - the most commonly executed operation.


## Array Insertions
1. Inserting a new element at the end of the Array.
    * **arr.append()**
2. Inserting a new element at the beginning of the Array.
    * **arr.insert(0, x)**
3. Inserting a new element at any given index inside the Array.
    * **arr.insert(n, x)**


## Array Deletions
1. Deleting the last element of the Array.
    * **arr.pop()**, **del arr[len(arr)-1]**
2. Deleting the first element of the Array.
    * **arr.pop(0)**, **del arr[0]**
3. Deletion at any given n-th index.
    * **arr.pop(n)**, **del arr[n]**
4. Deleting the first appearing element x of the Array.
    * **arr.remove(x)**


## Search in an Array
* Searching is the most important operation of an Array.
* Searching means to **find an occurrence of a particular element** in the Array and return its position. 
* Search becomes a constant time operation if we know the index in the Array that contains the element.
    + Simply go to the given index and check whether the element is there.

### Linear Search
* If the index is not known, then we need to check every element in the Array.
* This technique for finding an element by checking through all elements one by one is known as the linear search algorithm.
* In the worst case, a linear search ends up checking the entire Array, ***O(N)***.

### Binary Search
* If the elements in the Array are in *sorted order*, then we can use binary search.
* Binary search **repeatedly look at the middle element** in the Array, and determine whether the element must be to the left, or to the right.
* Each time, we can halve the number of elements, making binary search a lot faster.
* However, if the data is not sorted, binary search cannot be applied.


## In-Place Array Operations
* In-place Array operations help to reduce space complexity.
* In-place Array operations are important for programming interviews, where there is *a focus on minimizing both time and space complexity* of algorithms.


## List Comprehension
* List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
* newList = [expression for item in iterable if condition == True]

#### Without list comprehension
```python
arr = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = []

for x in arr:
    if "a" in x:
        newList.append(x)

print(newList)
```

#### With list comprehension
```python
arr = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in arr if "a" in x]

print(newList)
```
