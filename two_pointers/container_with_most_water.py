class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1

        max_capacity = 0
        current_capacity = 0
        while i != j:
            current_capacity = min(height[i],height[j])*(j - i)
            if current_capacity > max_capacity:
                max_capacity = current_capacity

            if height[i] < height[j]:
                i = i + 1
            else:
                j = j - 1
        
        return max_capacity