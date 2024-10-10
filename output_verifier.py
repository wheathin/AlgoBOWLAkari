# works by running cmd output_verifier.py [INPUT] [OUTPUT]

import sys

i_filename = sys.argv[1]
o_filename = sys.argv[2]

# Grid represented as [num row][num col]
i_grid = []
o_grid = []

# gets input grid
in_file = open(i_filename, 'r')

i_info = in_file.readline().split()

rows = int(i_info[0])
cols = int(i_info[1])

print("Rows:", rows, "/ Cols:", cols)

for i in range(rows):
    i_grid.append(in_file.readline().strip('\n'))
    
in_file.close()

# gets output grid
out_file = open(o_filename, 'r')

# if violation count not stated then errors
try:
    vio = int(out_file.readline())
except ValueError:
    print("INVALID VIOLATION COUNT")
    quit()

# reads until end of file and checks rows matching length
for i in range(rows):
    try:
        o_grid.append(out_file.readline().strip('\n'))
        if (cols != len(o_grid[-1])):
            print("INVALID NOT EQUAL COLS")
            quit()
    except EOFError:
            print("INVALID NOT EQUAL ROWS")
            quit()

out_file.close()

v_cou = 0

# tests if proper number of lights around number block
def test_num(r, c, num):
    lights = 0
    
    if (r != 0):
        if (o_grid[r-1][c] == 'L'):
            lights += 1
    if (r != rows-1):
        if (o_grid[r+1][c] == 'L'):
            lights += 1
    if (c != 0):
        if (o_grid[r][c-1] == 'L'):
            lights += 1
    if (c != cols-1):
        if (o_grid[r][c+1] == 'L'):
            lights += 1

    if (lights == num):
        return True
    else:
        return False

# tests for light collisions
def test_light(r, c):
    if (r != rows-1):
        for i in range(r+1, rows):
            if (o_grid[i][c] == 'L'):
                return False
            elif (o_grid[i][c] != '.'):
                break
    if (r != 0):
        for i in reversed(range(r)):
            if (o_grid[i][c] == 'L'):
                return False
            elif (o_grid[i][c] != '.'):
                break
    if (c != cols-1):
        for j in range(c+1, cols):
            if (o_grid[r][j] == 'L'):
                return False
            elif (o_grid[r][j] != '.'):
                break
    if (c != 0):
        for j in reversed(range(c)):
            if (o_grid[r][j] == 'L'):
                return False
            elif (o_grid[r][j] != '.'):
                break

    return True

# makes sure input grid matches output grid
def test_match(r, c):
    if (i_grid[r][c] == '.'):
        if (o_grid[r][c] == 'L' or o_grid[r][c] == '.'):
            return True
    else:
        if (o_grid[r][c] == i_grid[r][c]):
            return True
        else:
            return False

# tests for if blank spot is lit
def test_blank(r, c):
    if (r != rows-1):
        for i in range(r+1, rows):
            if (o_grid[i][c] == 'L'):
                return True
            elif (o_grid[i][c] != '.'):
                break
    if (r != 0):
        for i in reversed(range(r)):
            if (o_grid[i][c] == 'L'):
                return True
            elif (o_grid[i][c] != '.'):
                break
    if (c != cols-1):
        for j in range(c+1, cols):
            if (o_grid[r][j] == 'L'):
                return True
            elif (o_grid[r][j] != '.'):
                break
    if (c != 0):
        for j in reversed(range(c)):
            if (o_grid[r][j] == 'L'):
                return True
            elif (o_grid[r][j] != '.'):
                break
    return False

# checks each square in grid for validation
for r in range(rows):
    for c in range(cols):
        if (not test_match(r, c)):
            print(r, c)
            print("MISMATCH GRID")
            quit()
        match o_grid[r][c]:
            case '0' | '1' | '2' | '3' | '4':
                if(not test_num(r, c, int(i_grid[r][c]))):
##                    print(r, c, "NUM")
                    v_cou += 1
            case 'L':
                if(not test_light(r, c)):
##                    print(r, c, "LIGHT")
                    v_cou += 1
            case 'X':
                continue
            case '.':
                if(not test_blank(r, c)):
                    print(r, c)
                    print("INVALID SOLUTION")
                    quit()
            case _:
                print("INVALID GRID")
                quit()

print("VIOLATIONS STATED:", vio, "/ VIOLATIONS COUNTED:", v_cou)
