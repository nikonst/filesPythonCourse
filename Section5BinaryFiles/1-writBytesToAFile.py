# Pass "wb" to write a new file, or "ab" to append
with open("test.txt", "wb") as binary_file:
    # Write text or bytes to the file
    binary_file.write(b"Write text by encoding")
    num_bytes_written = binary_file.write(b'\xDE\xAD\xBE\xEF')
    print("Wrote %d bytes." % num_bytes_written)

# https://www.tutorialspoint.com/How-to-write-binary-data-to-a-file-using-Python

f = open('my_file', 'wb')
byte_arr = [120, 3, 255, 0, 100]
binary_format = bytearray(byte_arr)
f.write(binary_format)
f.close()


# https://diego.assencio.com/?index=99d3134bb98fdcc9a7c2bd6071db737d
output_file = open("myfile.bin","wb")
output_file.write(b"\x0a\x1c\x2c")
output_file.write(b"\x3d\x4e\x5f")
output_file.close()

# $hexdump -C myfile.bin

#test read binary
fin = open("myfile.bin", "rb")
data = fin.read()
print(data)
fin.close()


# *****************************************
# https://www.youtube.com/watch?v=qnKX1y7HAyE
# https://www.youtube.com/watch?v=eR3HQV3VfV0

# https://www.youtube.com/watch?v=Hp2fiB7cLO0

# https://www.youtube.com/watch?v=ghLiGHpmhgg
