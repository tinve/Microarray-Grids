__author__ = 'galina'

import os
import shutil

directory = "test"
new_directory = "shifted"

directory_to_write = os.path.join(directory, new_directory)

print directory_to_write
print os.listdir(directory_to_write)

shutil.rmtree(directory_to_write)

# path_to_write = os.path.join(directory_path, os.path.basename(path)) #write to new folder under old name
