import os
import pathlib


def write_files(path, file_num):
    for index in range(file_num):
        with open(f"{path}/file_{index}.txt", "w") as file:
            file.write(f"This is the 1st line of file {index}\n")
            file.write(f"This is the 2nd line of file {index}\n")
            file.write(f"This is the 3rd line of file {index}\n")
            file.write(f"This is the 4th line of file {index}\n")
            file.write(f"This is the 5th line of file {index}\n")
    return "Completed"


def all_lines(path):
    file_names = os.listdir(path)
    for file_name in sorted(file_names):
        file_path = os.path.join(path, file_name)
        for line in open(file_path):
            try:
                yield line
            except OSError:
                pass


print(write_files("./all_files", 5))
print(list(all_lines("./all_files")))
print(len(list(all_lines("./all_files"))))
