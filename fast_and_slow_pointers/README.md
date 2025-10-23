# Cycle Detection in Linked List

This project demonstrates how to detect a cycle in a singly linked list using the **Fast and Slow Pointer** (Floyd’s Tortoise and Hare) algorithm.

## 🚀 Algorithm
- Use two pointers:
  - **Slow pointer** moves one step at a time.
  - **Fast pointer** moves two steps at a time.
- If the list has a cycle, the two pointers will eventually meet.
- If the fast pointer reaches the end (`None`), the list has no cycle.

## 🧩 Code Example
```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```



## 🕒 Complexity

Time: O(n)

Space: O(1)

## 📘 Reference

Floyd’s Cycle Detection Algorithm (Tortoise and Hare)
