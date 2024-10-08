# works by running cmd algorithm_solver_ew.py [INPUT] [OUTPUT_NAME]

import sys

i_filename = sys.argv[1]
o_filename = sys.argv[2]

# gets input grid
in_file = open(i_filename, 'r')

i_info = in_file.readline().split()

rows = int(i_info[0])
cols = int(i_info[1])

print("Rows:", rows, "/ Cols:", cols)

# Grid represented as [num row][num col]
i_grid = []

for r in range(rows):
    full_row = in_file.readline().strip('\n')
    t_grid = []
    for c in range(cols):
        t_grid.append(full_row[c])
    i_grid.append(t_grid)
    
in_file.close()

akari_lights = []
akari_lights_r = []

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
    
# counts number of lights on space
def test_blank(r, c):
    lights = 0
    
    if (r != rows-1):
        for i in range(r+1, rows):
            if (i_grid[i][c] == 'L'):
                lights += 1
            elif (i_grid[i][c] != '.'):
                break
    if (r != 0):
        for i in reversed(range(r)):
            if (i_grid[i][c] == 'L'):
                lights += 1
            elif (i_grid[i][c] != '.'):
                break
    if (c != cols-1):
        for j in range(c+1, cols):
            if (i_grid[r][j] == 'L'):
                lights += 1
            elif (i_grid[r][j] != '.'):
                break
    if (c != 0):
        for j in reversed(range(c)):
            if (i_grid[r][j] == 'L'):
                lights += 1
            elif (i_grid[r][j] != '.'):
                break
    return lights

for r in range(rows):
    for c in range(cols):
        match i_grid[r][c]:
            case '0' | '1' | '2' | '3' | '4' | 'X':
                if (c < (cols - 1)):
                    akari_lights.append((r, c + 1))
                if (r < (rows - 1)):
                    akari_lights_r.append((r + 1, c))
            case '.':
                if (c == 0):
                    akari_lights.append((r, c))
                if (r == 0):
                    akari_lights_r.append((r, c))
            case _:
                print("INVALID GRID")
                quit()

# it finds all spots after a solid block in a row and column and then runs through to find the spot with the least violations to place the light
# really simple lots of violations doesnt account for number blocks at all but it solves

for l in akari_lights:
    place_r = l[0]
    place_c = l[1]
    p_lights = test_blank(l[0], l[1])
    blanks = True
    space_lit = 0
    if (p_lights > 0):
        space_lit += 1
    i = 1
    
    while blanks and (l[1] + i < (cols - 1)):
        match i_grid[l[0]][l[1] + i]:
            case '0' | '1' | '2' | '3' | '4' | 'X':
                blanks = False
            case '.':
                lights = test_blank(l[0], l[1] + i)
                if (lights < p_lights):
                    place_c = l[1] + i
                    p_lights = lights
                if (p_lights > 0):
                    space_lit += 1
                i += 1
            case 'L':
                space_lit = i
                blanks = False
            case _:
                print("INVALID LIGHT")
                quit()

    if (i != space_lit) and (i_grid[place_r][place_c] == '.'):
        i_grid[place_r][place_c] = 'L'
    
for l in akari_lights_r: 
    place_r = l[0]
    place_c = l[1]
    p_lights = test_blank(l[0], l[1])
    blanks = True
    space_lit = 0
    if (p_lights > 0):
        space_lit += 1
    i = 1
    
    while blanks and (l[0] + i < (rows - 1)):
        match i_grid[l[0] + i][l[1]]:
            case '0' | '1' | '2' | '3' | '4' | 'X':
                blanks = False
            case '.':
                lights = test_blank(l[0] + i, l[1])
                if (lights < p_lights):
                    place_r = l[0] + i
                    p_lights = lights
                if (p_lights > 0):
                    space_lit += 1
                i += 1
            case 'L':
                space_lit = i
                blanks = False
            case _:
                print("INVALID LIGHT")
                quit()

    if (i != space_lit) and (i_grid[place_r][place_c] == '.'):
        i_grid[place_r][place_c] = 'L'


v_cou = 0

# tests if proper number of lights around number block
def test_num(r, c, num):
    lights = 0
    
    if (r != 0):
        if (i_grid[r-1][c] == 'L'):
            lights += 1
    if (r != rows-1):
        if (i_grid[r+1][c] == 'L'):
            lights += 1
    if (c != 0):
        if (i_grid[r][c-1] == 'L'):
            lights += 1
    if (c != cols-1):
        if (i_grid[r][c+1] == 'L'):
            lights += 1

    if (lights == num):
        return True
    else:
        return False

# tests for light collisions
def test_light(r, c):
    if (r != rows-1):
        for i in range(r+1, rows):
            if (i_grid[i][c] == 'L'):
                return False
            elif (i_grid[i][c] != '.'):
                break
    if (r != 0):
        for i in reversed(range(r)):
            if (i_grid[i][c] == 'L'):
                return False
            elif (i_grid[i][c] != '.'):
                break
    if (c != cols-1):
        for j in range(c+1, cols):
            if (i_grid[r][j] == 'L'):
                return False
            elif (i_grid[r][j] != '.'):
                break
    if (c != 0):
        for j in reversed(range(c)):
            if (i_grid[r][j] == 'L'):
                return False
            elif (i_grid[r][j] != '.'):
                break

    return True

# tests for if blank spot is lit
def test_right(r, c):
    if (r != rows-1):
        for i in range(r+1, rows):
            if (i_grid[i][c] == 'L'):
                return True
            elif (i_grid[i][c] != '.'):
                break
    if (r != 0):
        for i in reversed(range(r)):
            if (i_grid[i][c] == 'L'):
                return True
            elif (i_grid[i][c] != '.'):
                break
    if (c != cols-1):
        for j in range(c+1, cols):
            if (i_grid[r][j] == 'L'):
                return True
            elif (i_grid[r][j] != '.'):
                break
    if (c != 0):
        for j in reversed(range(c)):
            if (i_grid[r][j] == 'L'):
                return True
            elif (i_grid[r][j] != '.'):
                break
    return False

# checks each square in grid for validation
first = True
for r in range(rows):
    for c in range(cols):
        match i_grid[r][c]:
            case '0' | '1' | '2' | '3' | '4':
                if(not test_num(r, c, int(i_grid[r][c]))):
                    v_cou += 1
            case 'L':
                if(not test_light(r, c)):
                    v_cou += 1
            case 'X':
                continue
            case '.':
                if(not test_right(r, c) and first):
                    print("INVALID SOLUTION")
                    first = False
            case _:
                print("INVALID GRID")
                quit()

out_file = open(o_filename, 'w')

out_file.write(str(v_cou))
for r in range(rows):
    line = '\n'
    for c in range(cols):
        line += i_grid[r][c]
    out_file.write(line)

out_file.close()
        
