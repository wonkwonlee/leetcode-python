# Array
* An Array is a collection of items - The items are stored in contiguous memory locations.
* The two most primitive Array operations are writing elements and reading elements.
* The capacity of an Array can be checked by len(arr)


## List Comprehension
* List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
* newlist = [expression for item in iterable if condition == True]

#### Without list comprehension
```python
    arr = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = []

    for x in arr:
      if "a" in x:
        newlist.append(x)

    print(newlist)
```
#### With list comprehension
```python
    arr = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in arr if "a" in x]

    print(newlist)
```
