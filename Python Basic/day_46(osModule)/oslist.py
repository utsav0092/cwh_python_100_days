import os
folders = os.listdir("data")

print(folders)

"""To know which directory you are working in """
print(os.getcwd())

"""To change the working directory"""
os.chdir("/Users")

print(os.getcwd())

"""Print the data in data files"""
# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))
