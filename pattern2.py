rows = 6

for i in range(rows):
    spaces = rows - 1 - i
    pattern = i + 1
    print(' ' * spaces + '1' * pattern)