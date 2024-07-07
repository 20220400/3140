import os
from Crypto.Hash import SHA256

def file_output(directory_path):
    files = os.listdir(directory_path)
    exe_files = [file for file in files if file.endswith(".exe")]
    return exe_files

def read_file_output(file_list, directory_path):
    file_output_dict = {}
    for file_name in file_list:
        file_path = os.path.join(directory_path, file_name)
        with open(file_path, "rb") as f:
            file_content = f.read()
            file_output_dict[file_name] = file_content
    return file_output_dict

def hash_output(content_dict):
    hash_output_dict = {}
    for file_name, content in content_dict.items():
        hasher = SHA256.new()
        hasher.update(content)
        hash_output_dict[file_name] = hasher.hexdigest()
    return hash_output_dict

def hash_match(hash_dict, match):
    for key, value in hash_dict.items():
        if value == match:
            return key, value
    return None, None

def main():
    with open("/home/cse/Lab3/Q2hash.txt", "r") as hash_match_file:
        hash_contents = hash_match_file.read().strip()

    current_dir = os.getcwd()
    exe_files = file_output(current_dir)
    file_contents = read_file_output(exe_files, current_dir)
    output_hash = hash_output(file_contents)
    matched_file, matched_hash = hash_match(output_hash, hash_contents)
    
    if matched_file is not None:
        print("Matched file:", matched_file)
        print("Hash code:", matched_hash)
        print("Match Hash:", hash_contents)
    else:
        print("No matching file found for hash:", hash_contents)

if __name__ == "__main__":
    main()
