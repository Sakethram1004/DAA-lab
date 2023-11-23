def place(row, col):
    for i in range(row):
        if x[i] == col or abs(x[i] - col) == abs(i - row):
            return False
    return True

def print_board(x):
    for i in range(len(x)):
        temp = [0] * len(x)
        temp[x[i]] = i + 1
        print(temp)
    exit(0)

def n_queens(row, n):
    for i in range(n):
        if place(row, i):
            x[row] = i
            if row == n - 1:
                print_board(x)
                break
            else:
                n_queens(row + 1, n)

n = int(input("Enter the number of Queens: "))
x = [-1] * n
print("The possible arrangements of Queens on the chessboard are: ")
n_queens(0, n)
