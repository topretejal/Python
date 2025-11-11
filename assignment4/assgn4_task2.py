try:
    file_name="output.txt"
    with open(file_name,"wt") as fh:
        txt = input("Enter text to write to the file:")
        fh.write(f"{txt}\n")
        print(f"Data successfully written to {file_name}\n")
    with open(file_name,"at") as fh:
        txt = input("Enter additional text to append:")
        fh.write(f"{txt}\n")
        print(f"Data successfully appended.\n")
    with open(file_name,"rt") as fh:
        print(f"Final content of {file_name}:")
        while True:
            line = fh.readline()
            if not line:
                break
            print(line.rstrip())
except Exception as err:
    print(f"Error: {err}")

