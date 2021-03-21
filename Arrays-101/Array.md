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
    * arr.append()
2. Inserting a new element at the beginning of the Array.
    * arr.insert(0, x)
3. Inserting a new element at any given index inside the Array.
    * arr.insert(n, x)


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
