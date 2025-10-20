# 🧩 N-Queens Solver (Python)

This is a Python implementation of the classic **N-Queens problem** using **recursive backtracking**.

The goal is to place `N` queens on an `N×N` chessboard such that no two queens threaten each other — i.e., no two queens share the same row, column, or diagonal.

---

## 🚀 How It Works

- The algorithm places one queen per row.
- Before placing a queen, it checks if the position is **safe** (no conflicts with existing queens).
- If safe, it places the queen and recursively moves to the next row.
- Once all rows are filled, the board configuration is saved as a valid solution.

---

## 📌 Features

- Solves the N-Queens problem for any `N ≥ 1`.
- Uses a simple array to represent board state efficiently.
- Prints all valid board configurations in a readable format.
- Displays the total number of solutions found.

---

## 🖥️ Usage

### 1. Run the script

```bash
$ python n_queens.py
```

### 2. Enter number of queens when prompted:
```
Enter the number of queens: 4
```

### 3. Example Output:
```
Number of solutions = 2

Solution 1:
 Q  
   Q
Q
  Q

Solution 2:
  Q
Q
   Q
 Q
```

### Concepts Used

- Backtracking

- Recursion

- Array-based board representation (each index is a row, value is column)

### File Structure
```
n_queens.py      # Main Python script
README.md        # Project documentation
```

