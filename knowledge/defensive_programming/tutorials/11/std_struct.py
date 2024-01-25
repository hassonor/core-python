import struct

# 11.3: Working with Binary Data Record Layouts

# Open the ZIP file in binary read mode
with open('myfile.zip', 'rb') as f:
    data = f.read()

start = 0  # Initialize the start position for reading the data

# Loop to process the first 3 file headers
for i in range(3):
    start += 14  # Skip the first 14 bytes to reach the start of the interesting part of the file header

    # Unpack data from the next 16 bytes. This gives us:
    # crc32: A checksum for the file
    # comp_size: The size of the compressed file
    # uncomp_size: The size of the uncompressed file
    # filenamesize: The length of the filename field
    # extra_size: The length of the extra field
    fields = struct.unpack('<IIIHH', data[start:start + 16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16  # Move past the unpacked bytes

    # Extract the filename using its length (filenamesize)
    filename = data[start:start + filenamesize]
    start += filenamesize  # Move past the filename field

    # Extract the extra field using its length (extra_size)
    extra = data[start:start + extra_size]
    # Print the information for this file
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size  # Move to the start of the next file header
