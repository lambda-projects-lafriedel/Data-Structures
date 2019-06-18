Answer the following questions for each of the data structures you implemented as part of this project.

## Queue

1. What is the runtime complexity of `enqueue`?
It is O(1) / constant time, because each step is only performed once; the value of the parameter does not affect the amount of times the steps run. It consistently only adds one item.

2. What is the runtime complexity of `dequeue`?
It is O(1) / constant time, because each step is only performed once. It consistently removes only one item.

3. What is the runtime complexity of `len`?
It is O(1) / constant time, because grabbing the length is very fast. It does not need to enumerate over the elements to get the length.

## Binary Search Tree

1. What is the runtime complexity of `insert`? 
Assuming our tree remains fairly balanced, it is at worst O(n) where n is the height of the tree.
 
2. What is the runtime complexity of `contains`?
Similar to `insert`, it is at worst O(n), where n is the height of the tree. 

3. What is the runtime complexity of `get_max`? 
It is O(n) where n is the height of the tree. It is guaranteed to run the entire height of the tree, as the highest value will always be in the last spot it needs to hit.

## Heap

1. What is the runtime complexity of `_bubble_up`?
It is O(log n) where n is the length of the list/height of the tree. In each iteration of the loop, the parent index is essentially half of the passed index, therefore decreasing the amount of steps by about half until the loop breaks.

2. What is the runtime complexity of `_sift_down`?
It is O(log n) where n is the length of the list/height of the tree. By starting at index 0, multiplying it by 2 and adding 1 or 2, and then setting the index at whichever child index was swapped, it slowly halves the number of operations.

3. What is the runtime complexity of `insert`?
It is O(log n), where n is the length of the list/height of the tree. It relies mostly on _bubble_up which has a runtime of O(log n), the only line before _bubble_up is called has a time complexity of O(1), so we take the more complex runtime as the answer.

4. What is the runtime complexity of `delete`?
It's most expensive line is calling `_sift_down`, so it is O(log n). The rest of the lines are O(1).

5. What is the runtime complexity of `get_max`?
O(1) because it is only ever performing 1 action regardless of tree height.

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
It is O(1), because it's only inserting one item and the amount of operations does not change. Even if it's being inserted near the beginning of a long list, it only needs to reassign one next and one prev value.

2. What is the runtime complexity of `ListNode.insert_before`?
Same as above -- O(1) since it's only reassigning one next and one prev value.

3. What is the runtime complexity of `ListNode.delete`?
O(1), as it's always removing only one value per call, and the amount of operations are not dynamic.

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1) -- function runs the same amount of time every time, and the number of operations is not dynamic to any value being passed in.

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1) -- function runs the same amount of time every time, and the number of operations does not increase or decrease for any reason.

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(1) -- function runs the same amount of time every time, and the number of operations is not dynamic to any value being passed in.

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(1) -- function runs the same amount of time every time, and the number of operations does not increase or decrease for any reason.

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(1) -- function runs the same amount of time every time, and the number of operations is not dynamic to any value being passed in.

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(1) -- function runs the same amount of time every time, and the number of operations is not dynamic to any value being passed in.

10. What is the runtime complexity of `DoublyLinkedList.delete`?
O(1) -- function runs the same amount of time every time, and the number of operations is not dynamic to any value being passed in.

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    Deleting from a doubly linked list is O(1), while Array.splice() is at worst O(n), because in its worst case it would have to copy over the entire array (n).