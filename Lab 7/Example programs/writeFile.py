# Open file for output
outfile = open("test.txt", "w") # w means open for writing. 

# Write data to the file, adding a new line character \n wherever you want a new line.
outfile.write("Hiliary Clinton\n")
outfile.write("Bill Clinton\n")
outfile.write("George Bush\n")
outfile.write("Barack Obama\n")
outfile.write("Hiliary Clinton")

outfile.close() # Close the output file
