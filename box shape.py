def print_box_pattern(rows,cols):
    for i in range(rows):
        for j in range(cols):
            if (i==0 or i==rows-1 or j==0 or j==cols-1):
                print("*",end="")
            else:
                print(" ",end="")
        print()

num_rows=5
num_cols=5

print_box_pattern(num_rows,num_cols)
        
