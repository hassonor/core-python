import os

"""
This Python script demonstrates various methods from the 'os' module for directory and file handling.

- 'os.chdir(path)': Changes the current working directory to the specified path.
- 'os.getcwd()': Returns the current working directory.
- 'os.chmod(path, mode)': Changes the mode of a file or directory.
- 'os.mkdir(path, mode=0o777)': Creates a directory at the specified path.
- 'os.makedirs(path, mode=0o777, exist_ok=False)': Creates a directory, recursively creating parent directories if necessary.
- 'os.remove(path)': Removes (deletes) a file.
- 'os.path.exists(path)': Checks if a path exists.
- 'os.path.isdir(path)': Checks if the specified path is a directory.
"""

# os.chdir
"""
'os.chdir' changes the current working directory to the specified path.
Example: Change to the user's home directory
"""

home_directory = os.path.expanduser('~')
os.chdir(home_directory)

# os.getcwd
"""
'os.getcwd' returns a string representing the current working directory.
Example: current_directory = os.getcwd()
"""
current_directory = os.getcwd()
print(f'Current Directory: {current_directory}')

# os.chmod
"""
'os.chmod' changes the mode of the path to the numeric mode.
Example: os.chmod('/path/to/file_or_directory', 0o777)  # Read, write, and execute by all
"""
# os.chmod('/path/to/file_or_directory', 0o777)

# os.mkdir
"""
'os.mkdir' creates a directory named path with the specified numeric mode.
Example: os.mkdir('/path/to/new_directory')
"""
# os.mkdir('/path/to/new_directory')

# os.makedirs
"""
'os.makedirs' is used to create a directory recursively. That means it creates all the intermediate-level directories needed to contain the leaf directory.
Example: os.makedirs('/path/to/new/directory/structure', exist_ok=True)
"""
# os.makedirs('/path/to/new/directory/structure', exist_ok=True)

# os.remove
"""
'os.remove' removes (deletes) the file path.
Example: os.remove('/path/to/file')
"""
# os.remove('/path/to/file')

# os.path.exists
"""
'os.path.exists' is used to check whether the specified path exists or not.
Example: exists = os.path.exists('C://Users//Or//Desktop')
"""
exists = os.path.exists('C://Users//Or//Desktop')
print(f'Path Exists: {exists}')

# os.path.isdir
"""
'os.path.isdir' checks if the specified path is an existing directory.
Example: is_dir = os.path.isdir('C://Users//Or//Desktop')
"""
is_dir = os.path.isdir('C://Users//Or//Desktop')
print(f'Is Directory: {is_dir}')
