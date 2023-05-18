import os
import shutil

from_dir = "C:/Users/arnav/Downloads"
to_dir = "C:/Users/arnav/Documents"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    root,extension=os.path.splitext(file_name)
    print(root)
    print(extension)
