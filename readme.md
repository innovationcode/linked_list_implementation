# Linked List 
- A linked list is a linear data structure in which the elements are not stored at continuous memory location.
  
- A linked list is a collection of nodes where each node contains a data field and a reference (link) to the 
  next node in the list.

- linked list are very useful in dynamic memory allocation.

- Linked lists are handy if you need to insert items in between or remove items. 
  ( With an array, you would need to move lots of elements ‘to the right’ to make room for a new element in the middle or ‘to the left’ to fill the hole if you remove an element in the middle.)

- Linked lists are often sorted in some way and you want to maintain the proper order at all times. Although they allow for fast removal and insertion, 
  they have poor cache performance due to poor space locality: all nodes can be ‘anywhere’ in memory, they are not at neat consecutive locations. Also, the pointers to the next node (and previous node in case of double linked list) take extra memory.
  


