\# Cycle Detection in Linked List



This project demonstrates how to detect a cycle in a singly linked list using the \*\*Fast and Slow Pointer\*\* (Floyd’s Tortoise and Hare) algorithm.



\## 🚀 Algorithm

\- Use two pointers:

&nbsp; - \*\*Slow pointer\*\* moves one step at a time.

&nbsp; - \*\*Fast pointer\*\* moves two steps at a time.

\- If the list has a cycle, the two pointers will eventually meet.

\- If the fast pointer reaches the end (`None`), the list has no cycle.



\## 🧩 Code Example

```python

def hasCycle(head):

&nbsp;   slow = fast = head

&nbsp;   while fast and fast.next:

&nbsp;       slow = slow.next

&nbsp;       fast = fast.next.next

&nbsp;       if slow == fast:

&nbsp;           return True

&nbsp;   return False



🕒 Complexity



Time: O(n)



Space: O(1)



📘 Reference



Floyd’s Cycle Detection Algorithm (Tortoise and Hare)

