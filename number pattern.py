def print_pattern(rows):
    #for i in range(1, rows +1):
    for i in range(1,rows+1):
        #for j in range(i, 0, -1):
        for j in range(1,i+1):
            print(j, end=" ")
        print()

num_rows =int(input("enter a number"))
print_pattern(num_rows)
