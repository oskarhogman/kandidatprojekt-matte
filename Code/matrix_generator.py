import numpy as np

def read_input(input_str):
    top_row, diff = input_str.split(':')

    top_row = [int(x) for x in top_row.split()]
    diff = [int(x) for x in diff.split()]

    while len(diff) > len(top_row):
        top_row.append(0)

    return top_row, diff

def get_variables(diff_len):
    variables = list()
    for i in range(1, diff_len + 1):
        for j in range(1, i + 1):
            variables.append((i,j))
    return variables

def rc_to_matrixcol(r,c):
    # Givet var-index var den befinner sig i variables
    return int(r*(r-1)/2 + c - 1)

def create_matrix(top_row, diff):
    A = list()
    b = list()

    n = len(diff)
    numvar = rc_to_matrixcol(n,n) + 1

    for c in range(1, n+1):
        temp1 = [0]*numvar
        temp2 = [0]*numvar
        temp1[rc_to_matrixcol(n,c)] = 1
        temp2[rc_to_matrixcol(n,c)] = -1
        A.append(temp1)
        A.append(temp2)
        b.append(top_row[c-1])
        b.append(-top_row[c-1])

    for r in range(1, n):
        for c in range(1, r+1):
            temp = [0]*numvar
            temp[rc_to_matrixcol(r,c)] = 1
            temp[rc_to_matrixcol(r+1,c)] = -1
            A.append(temp)
            b.append(0)

    for r in range(1, n):
        for c in range(1, r+1):
            temp = [0]*numvar
            temp[rc_to_matrixcol(r,c)] = -1
            temp[rc_to_matrixcol(r+1,c+1)] = 1
            A.append(temp)
            b.append(0)
    
    for r in range(1, n):
        temp1 = [0]*numvar
        temp2 = [0]*numvar
        for c in range(1, r+1):
            temp1[rc_to_matrixcol(r,c)] = 1
            temp2[rc_to_matrixcol(r,c)] = -1
        A.append(temp1)
        A.append(temp2)
        b.append(sum(diff[:r]))
        b.append(-sum(diff[:r]))
    
    return A, b

def create_jl_line(input_str, A, b):
    A_out = "["
    b_out = "["

    for line in A:
        line_len = len(line)
        for index, nr in enumerate(line):
            if index == line_len-1:
                A_out += str(nr) + "; "
            else:
                A_out += str(nr) + " "
    A_out = A_out[:-2] + ']'

    line_len = len(b)
    for index, nr in enumerate(b):
        b_out += str(nr) + "; "
    b_out = b_out[:-2] + ']'

    if len(A_out) < 2 or len(b_out) < 2:
        A_out = '[]'
        b_out = '[]'

    out_line = 'polytope = "' + input_str.strip() + '"; '\
        + 'A = ' + A_out + '; ' + 'b = ' + b_out
    return out_line

def write_file(filename, julia_filename):
    with open(filename, 'r') as file_in, open(julia_filename, 'w') as file_out:
        for line in file_in:
            top_row, diff = read_input(line.strip())
            A, b = create_matrix(top_row, diff)
            out = create_jl_line(line, A, b)
            print(out, file=file_out)

write_file('test.txt', 'test.jl')

#top_row, diff = read_input('3 2 1:2 1 1 1 1')
#variables = get_variables(len(diff))
#create_matrix(top_row, diff)
