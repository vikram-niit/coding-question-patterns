# for each row 
# check safety
# place queen
# call recursively to place the next queen in the next row
# base condition - when all rows are finished
# After all columns in each row are traversed

def solve_n_queens(board):
	
	def is_safe(board, row, col):
		for i in range(row):
			if board[i] - i == col - row:
				return False
			elif board[i] + i == col + row:
				return False
			elif board[i] == col:
				return False
		return True
				
	def solve(board, row):
		print(f"row = {row}")
		if row == n:
			print(f"solution = {board}")
			solutions.append(board[:])
			return
		for col in range(n):
			if is_safe(board, row, col):
				board[row] = col
				solve(board, row + 1)
	solutions = []
	solve(board, 0)
	return solutions

def print_solutions(solutions):
	for board in solutions:
		for i in range(len(board)):
			print(f"{'*' * board[i]}X{'*' * (n - board[i])}")
		print("\n\n")
	
		
if __name__ == '__main__':
	n = input("Enter the number of queens")
	n = int(n)
	board = [-1] * n
	solutions= solve_n_queens(board)
	print(f"solutions = {solutions}")
	print(f"Number of solutions = {len(solutions)}")
	print_solutions(solutions)
