"""
Kth Largest Element in an Array
--------------------------------
Find the kth largest element in an unsorted array.
"""

import heapq

def find_kth_largest(nums, k):
    """
    Return the kth largest element in the array.
    Uses a min-heap of size k.

    :param nums: List[int] - input array
    :param k: int - which largest element to find
    :return: int - kth largest element
    """
    # Min-heap to store k largest elements
    heap = []
    
    for num in nums:
        heapq.heappush(heap, num)
        # Maintain heap size of k
        if len(heap) > k:
            heapq.heappop(heap)
    
    # Root of the heap = kth largest
    return heap[0]


if __name__ == "__main__":
    # Example usage
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print(find_kth_largest(nums, k))  # Output: 5
