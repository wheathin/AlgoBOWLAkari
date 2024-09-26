# this is entirely just to make a stupid input
rows = 420
cols = 69

##make row
fin_row = ".4." * int(cols / 3)
emp_row = "." * cols

f_out = open("funny_input.txt", "w")

f_out.write(str(rows) + ' ' + str(cols) + "\n")

##fin_row = "L4L" * int(cols / 3)
##emp_row = "L" * cols
##
##f_out = open("funny_output.txt", "w")
##
##f_out.write(str(25760)+ "\n")

            
for r in range(int(rows / 3)):
    f_out.write(emp_row + "\n")
    f_out.write(fin_row + "\n")
    f_out.write(emp_row + "\n")

f_out.close()

print("Finished generating")
