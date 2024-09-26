# pip install shutup to suppress deprecated warning
# if this is breaking stuff can delete
import shutup
shutup.mute_warnings()

# Grid represented as [num row][num col]
grid = []

# if violation count not stated then errors
try:
    vio = int(input())
except ValueError:
    print("INVALID VIOLATION COUNT")
    quit()
    
fin = False
rows = 0

# reads until end of file and checks rows matching length
while(not fin):
    try:
        grid.append(input())
        rows += 1
        if (len(grid[0]) != len(grid[-1])):
            print("INVALID GRID")
            quit()
    except EOFError:
        fin = True

cols = len(grid[0])
v_cou = 0

print("Rows:", rows, "/ Cols:", cols)

# tests if proper number of lights around number block
def test_num(r, c, num):
    lights = 0
    
    if (r != 0):
        if (grid[r-1][c] == 'L'):
            lights += 1
    if (r != rows-1):
        if (grid[r+1][c] == 'L'):
            lights += 1
    if (c != 0):
        if (grid[r][c-1] == 'L'):
            lights += 1
    if (c != cols-1):
        if (grid[r][c+1] == 'L'):
            lights += 1

    if (lights == num):
        return True
    else:
        return False

# tests for light collisions
def test_light(r, c):
    if (r != rows-1):
        for i in range(r+1, rows):
            if (grid[i][c] == 'L'):
                return False
            elif (grid[i][c] != '.'):
                break
    if (r != 0):
        for i in reversed(range(r)):
            if (grid[i][c] == 'L'):
                return False
            elif (grid[i][c] != '.'):
                break
    if (c != cols-1):
        for j in range(c+1, cols):
            if (grid[r][j] == 'L'):
                return False
            elif (grid[r][j] != '.'):
                break
    if (c != 0):
        for j in reversed(range(c)):
            if (grid[r][j] == 'L'):
                return False
            elif (grid[r][j] != '.'):
                break

    return True

# tests for if blank spot is lit
def test_blank(r, c):
    if (r != rows-1):
        for i in range(r+1, rows):
            if (grid[i][c] == 'L'):
                return True
            elif (grid[i][c] != '.'):
                break
    if (r != 0):
        for i in reversed(range(r)):
            if (grid[i][c] == 'L'):
                return True
            elif (grid[i][c] != '.'):
                break
    if (c != cols-1):
        for j in range(c+1, cols):
            if (grid[r][j] == 'L'):
                return True
            elif (grid[r][j] != '.'):
                break
    if (c != 0):
        for j in reversed(range(c)):
            if (grid[r][j] == 'L'):
                return True
            elif (grid[r][j] != '.'):
                break
    return False

# checks each square in grid for validation
for r in range(rows):
    for c in range(cols):
        match grid[r][c]:
            case '1':
                if(not test_num(r, c, 1)):
                    v_cou += 1
            case '2':
                if(not test_num(r, c, 2)):
                    v_cou += 1
            case '3':
                if(not test_num(r, c, 3)):
                    v_cou += 1
            case '4':
                if(not test_num(r, c, 4)):
                    v_cou += 1
            case 'L':
                if(not test_light(r, c)):
                    v_cou += 1
            case 'X':
                continue
            case '.':
                if(not test_blank(r, c)):
                    print("INVALID SOLUTION")
                    quit()
            case _:
                print("INVALID GRID")
                quit()

print("VIOLATIONS STATED:", vio, "/ VIOLATIONS COUNTED:", v_cou)
