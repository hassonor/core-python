f1 = open("example.txt")

# first_line = f1.readline()
# second_line = f1.readline()

for line in f1:
    print(line, end="")

f1.close()

f2 = open("oop.py")
all_lines = f2.readlines()  # can also write list(f2)

for line in all_lines:
    if "self" in line:  # print all lines contains self
        print(line, end="")

# Open a file for write
f1 = open("my_text",
          "w")  # "a" (append) flag will add data to exist file at end or create a new file and add to start
f1.write("First line of file!\n")
f1.write("Second line\n")

print("Good morning Or Hasson and a nice day.", file=f1)

name = "Or Hasson"
user_id = 12345
major = "CS"
average = 91
line = "Name - {}, id {}, major - {} with average {}\n".format(name, user_id, major, average)
f1.write(line)

f1.write("Congratulation {} for achieving high grade!".format("Or Hasson"))

f1.close()

"""
Open Binary Files:
f = open('myfile.bin','rb') -> open for read
f = open('workfile','rb+') -> open for read and update
f = open('workflie','wb') -> open for write and override previous data on file if exist
"""

f = open('test.bin', "wb")
d = b'\x80\03]q\x00(k\x01'
print(type(d))
f.write(d)
f.close()

"""
This Python script demonstrates various file handling methods.

- 'seek(offset, whence=0)': Moves the file cursor to a specified position.
- 'tell()': Returns the current position of the file cursor.
- 'read(size)': Reads a specified number of bytes from the file.
- 'write(content)': Writes the given content to the file.
- 'flush()': Flushes the internal buffer, ensuring all writes are applied.
- 'writable()': Checks if the file is writable.
"""

# Open a file in read and write mode
with open('example.txt', 'r+') as file:
    # 'seek' method
    """ 
    The 'seek' method is used to change the current file cursor position.
    Here, we move the cursor to the 11th byte (10 bytes from the start).
    """
    file.seek(10)

    # 'tell' method
    """
    The 'tell' method returns the current position of the file cursor.
    After using 'seek', it should show the new cursor position.
    """
    current_position = file.tell()
    print(f'Current Position: {current_position}')

    # 'read' method
    """
    The 'read' method reads 'size' bytes from the file. If 'size' is not specified,
    it reads until the end of the file starting from the current cursor position.
    """
    content = file.read(5)
    print(f'Read Content: {content}')

    # 'write' method
    """
    The 'write' method writes the given string to the file at the current
    cursor position, overwriting any existing content at that position.
    """
    file.write('Hello World')

    # 'flush' method
    """
    The 'flush' method is used to flush the internal buffer, i.e., it
    forces the write buffer to be written to the file.
    """
    file.flush()

    # 'writable' method
    """
    The 'writable' method checks if the file stream allows writing.
    It returns True if the file is writable, and False otherwise.
    """
    is_writable = file.writable()
    print(f'Is File Writable? {is_writable}')
