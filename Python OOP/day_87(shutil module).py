import shutil
import os

shutil.copy("main.py", "main2.py")  # copy the file with content in new file
shutil.copytree(".tutorial", "my_tutorial")  # copy the whole file tree in new file
shutil.move(".filename/file.file", "new_file_name")   # create the content of filename to new_file_name
shutil.rmtree("my_tutorial")   # delete the directory
os.remove("file.file", )   # will remove the file
