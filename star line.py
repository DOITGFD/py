def print_pattern(rows):
    for i in range(1, rows + 1):
        for j in range(i):
            print(i, end=" ")
        print()

# Example usage:
num_rows = 5
print_pattern(num_rows)
