# 🧮 Evaluate Postfix Expression (RPN)

📘 **Problem**

Given a list of tokens representing an arithmetic expression in Reverse Polish Notation, evaluate it and return the result.

**Example**
```
Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
```

⚙️ **Approach**

Use a stack:

- Push operands onto the stack.  
- On encountering an operator, pop the top two operands, apply the operation, and push the result back.  
- At the end, the stack’s only element is the answer.

**Code (Python)**
```python
def evalRPN(tokens):
    stack = []
    for token in tokens:
        if token in "+-*/":
            b, a = stack.pop(), stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            else: stack.append(int(a / b))  # truncate toward zero
        else:
            stack.append(int(token))
    return stack[0]
```

⏱️ **Complexity**
- Time: O(n)  
- Space: O(n)

🧠 **Example Run**

["4","13","5","/","+"] → 6  
→ (4 + (13 / 5)) = 6
