rows = int(input("Enter the no of rows: "))

for i in range(rows):
    spaces = rows - 1 - i
    ast = 2 * i + 1
    print(' ' * spaces + '^' * ast)