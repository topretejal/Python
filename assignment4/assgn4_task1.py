try:
    file_name='sample.txt'
    with open(file_name, "rt") as fh:
        i=1
        while True:
            line = fh.readline()
            if not line:
                break
            print(f"Line {i}: {line.rstrip()}")
            i += 1
except FileNotFoundError as err:
    print(f"Error: The file '{file_name}' was not found.")

#for creating file and testing
# with open('sample.txt','xt') as fh:
#     fh.write("This is a sample file.\n")
#     fh.write("It contains multiple lines")