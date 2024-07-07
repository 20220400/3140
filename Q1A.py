import os

# reads a file in the current directory
def file_output(directory_path):
    files = os.listdir(directory_path)
    py_files = [file for file in files if file.endswith(".exe")]

    with open("output.txt", "w") as f:
        for file in py_files:
            f.write(file + "\n")

def main():
    current_dir = os.getcwd()
    file_output(current_dir)

if __name__ == "__main__":
    main()
