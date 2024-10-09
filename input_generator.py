# this is entirely just to make a stupid input
rows = 420
cols = 69

##make row
fin_row = ".4." * int(cols / 3)
emp_row = "." * cols

f_out = open("funny_output_manual.txt", "w")

##f_out.write(str(rows) + ' ' + str(cols) + "\n")

f_out.write('0\n')

##fin_row = "L4L" * int(cols / 3)
##emp_row = "L" * cols
##
##f_out = open("funny_output.txt", "w")
##
##f_out.write(str(25760)+ "\n")

o_grid = []
            
##for r in range(int(rows / 3)):
##    f_out.write(emp_row + "\n")
##    f_out.write(fin_row + "\n")
##    f_out.write(emp_row + "\n")

for r in range(int(rows / 3)):
    o_grid.append(emp_row)
    o_grid.append(fin_row)
    o_grid.append(emp_row)

for c in range(int(cols / 3)):
    up = (3* c) + 1
    left = (3 * c)
    right = (3 * c + 2)
    
    o_grid[3 * c] = o_grid[3 * c][0:up] + 'L' + o_grid[3 * c][up + 1:]
    o_grid[3 * c + 1] = o_grid[3 * c + 1][0:left] + 'L' + o_grid[3 * c + 1][left + 1:]
    o_grid[3 * c + 1] = o_grid[3 * c + 1][0:right] + 'L' + o_grid[3 * c + 1][right + 1:]
    o_grid[3 * c + 2] = o_grid[3 * c + 2][0:up] + 'L' + o_grid[3 * c + 2][up + 1:]

for f in range(int(cols / 3), int(rows/3)):
    o_grid[3 * f] = o_grid[3 * f][0:1] + 'L' + o_grid[3 * f][2:]
    o_grid[3 * f + 2] = o_grid[3 * f + 2][0:4] + 'L' + o_grid[3 * f + 2][5:]

for l in o_grid:
    f_out.write(l + "\n")

f_out.close()

print("Finished generating")
