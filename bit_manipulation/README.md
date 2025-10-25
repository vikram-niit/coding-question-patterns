1\. Basic Bit Operations



These are the building blocks of all bit manipulation questions.



AND (\&) – isolates bits



x \& 1  # check if last bit is 1 (odd number)

x \& ~(1 << k)  # set k-th bit to 0





OR (|) – sets bits



x | (1 << k)  # set k-th bit to 1





XOR (^) – toggles bits, detects differences



x ^ (1 << k)  # flip k-th bit

a ^ a == 0    # XOR of same numbers is 0





Shift operators (<<, >>) – multiply/divide by powers of 2



x << 1  # multiply by 2

x >> 1  # divide by 2



2\. Common Patterns

Pattern 1: Check if a number is a power of 2



Idea: Powers of 2 have only one bit set. x \& (x-1) removes the lowest set bit.



Code:



def is\_power\_of\_2(x):

&nbsp;   return x > 0 and (x \& (x-1)) == 0



Pattern 2: Count number of set bits



Idea: Keep removing the lowest set bit (x = x \& (x-1)) until x becomes 0.



Code:



def count\_set\_bits(x):

&nbsp;   count = 0

&nbsp;   while x:

&nbsp;       x \&= x - 1

&nbsp;       count += 1

&nbsp;   return count



Pattern 3: Find the only non-repeating element (XOR trick)



Idea: XOR all numbers; duplicates cancel out.



Code:



def single\_number(nums):

&nbsp;   result = 0

&nbsp;   for num in nums:

&nbsp;       result ^= num

&nbsp;   return result



Pattern 4: Swap two numbers without temp

a ^= b

b ^= a

a ^= b





Fun trick using XOR.



Pattern 5: Subsets / Power Set using Bits



Idea: Each subset can be represented as a bitmask of length n.



def subsets(nums):

&nbsp;   n = len(nums)

&nbsp;   res = \[]

&nbsp;   for mask in range(1 << n):

&nbsp;       subset = \[nums\[i] for i in range(n) if mask \& (1 << i)]

&nbsp;       res.append(subset)

&nbsp;   return res



Pattern 6: Rightmost set bit



Idea: x \& -x isolates the lowest set bit.



rightmost\_set\_bit = x \& -x



Pattern 7: Count bits for all numbers (0…n)



Idea: Dynamic programming using x \& (x-1) or x >> 1.



def countBits(n):

&nbsp;   dp = \[0] \* (n + 1)

&nbsp;   for i in range(1, n + 1):

&nbsp;       dp\[i] = dp\[i \& (i - 1)] + 1

&nbsp;   return dp



Pattern 8: Bit masking for subsets with constraints



Examples: “Find all subsets where sum is even,” or “subsets of size k.”



Usually done with bitmasks and counting set bits.



Pattern 9: XOR basis / Maximum XOR



Harder pattern: build a linear basis to maximize XOR of a subset.



Often shows up in competitive programming.



Pattern 10: Swap bits, reverse bits, or rotate bits



Bit tricks for manipulation in low-level coding or embedded systems.

