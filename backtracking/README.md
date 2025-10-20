\# 🧩 N-Queens Solver (Python)



This is a Python implementation of the classic \*\*N-Queens problem\*\* using \*\*recursive backtracking\*\*.



The goal is to place `N` queens on an `N×N` chessboard such that no two queens threaten each other — i.e., no two queens share the same row, column, or diagonal.



---



\## 🚀 How It Works



\- The algorithm places one queen per row.

\- Before placing a queen, it checks if the position is \*\*safe\*\*.

\- If safe, it places the queen and recursively places the next.

\- Once all rows are filled, the board configuration is saved as a solution.



---



\## 📌 Features



\- Solves the N-Queens problem for any `N ≥ 1`.

\- Prints all valid board configurations in a human-readable format.

\- Displays the total number of solutions.



---



\## 🖥️ Usage



Run the script:



```bash

$ python n\_queens.py



