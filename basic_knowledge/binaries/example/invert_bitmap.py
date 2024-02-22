import os

# source_file = 'bm_test.txt'
source_file = 'vintage-halloween-bat.bmp'
inverted_file = f'inverted-{source_file}'

with open(source_file, 'rb') as bat:  # No encoding
    # Read the 14 byte header
    file_header = bat.read(14)

    bmp_id = file_header[0:2]
    print(bmp_id)
    if bmp_id == b'BM':  # we have a Windows bitmap file
        file_size = int.from_bytes(file_header[2:6], 'little')
        print(f'File size in header: {file_size}')
        os_size = os.path.getsize(source_file)
        print(f'File size reported by the operating system: {os_size}')

        if file_size != os_size:
            print('File size does not match file header size. '
                  'Are you sure this is a bitmap file?')
        else:
            reserved = file_header[6:10]
            print(f'For information, reserved bytes are: {reserved}')

            offset = int.from_bytes(file_header[-4:], 'little')
            print(f'Bitmap data starts at: {offset}')

            # Now read the DIB header and other information.
            # We're not interested in most of these values, but
            # we'll need them when writing the inverted file.
            # We read all bytes from the current position to 'offset'.
            dib_header_etc = bat.read(offset - bat.tell())

            # Check DIB header size
            dib_header_size = int.from_bytes(dib_header_etc[0:4], 'little')

            # We're only going to process BITMAPINFOHEADER files
            print(f'Bitmap header is {dib_header_size} bytes')
            if dib_header_size == 40:
                image_width = int.from_bytes(dib_header_etc[4:8], 'little', signed=True)
                image_height = int.from_bytes(dib_header_etc[8:12], 'little', signed=True)
                print(f'image is {image_width} by {image_height}')

                # Get the pixel data size (in bytes)
                pixel_array_size = int.from_bytes(dib_header_etc[20:24], 'little')
                print(f'Size of pixel array (bytes) = {pixel_array_size}')

                # Check: we should now be at 'offset' in the file.
                current_position = bat.tell()
                print(f'File pointer is at position {current_position}')
                if current_position != offset:
                    print(f"Something's gone wrong. We're at {current_position}, should be at {offset}")

                bat.seek(offset)  # Strictly speaking, this is redundant.

                # Read `pixel_array_size` bytes to get the image pixel data
                image = bytearray(bat.read(pixel_array_size))

                for index, bite in enumerate(image):
                    # Reverse the bits in each byte
                    image[index] = bite ^ 255

                # Now read the remainder of the file (if any)
                remainder = bat.read()

                with open(inverted_file, 'wb') as inverted_bat:
                    print(f'\tWriting header')
                    inverted_bat.write(file_header)
                    print(f'\tWriting DIB header and other blocks')
                    inverted_bat.write(dib_header_etc)
                    print(f'\tWriting image data')
                    inverted_bat.write(image)
                    if remainder:
                        print(f'\tWriting remaining bytes')
                        inverted_bat.write(remainder)

                print(f'Image file {inverted_file} created.')
            else:
                print(f'{source_file} is not a supported bitmap format.')
    else:
        print(f'{source_file} does not appear to be a bitmap (.bmp) file.')

