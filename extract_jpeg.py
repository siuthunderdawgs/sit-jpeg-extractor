import sys

if len(sys.argv) == 2:
	filename_read  = sys.argv[1]
	filename_write = sys.argv[1] + ".jpg" 
elif len(sys.argv) == 3:
	filename_read  = sys.argv[1]
	filename_write = sys.argv[2]
else:
	print("Error: Wrong number of arguments!")
	print("Please provide either 1 argument or 2 arguments:")
	print("1st Argument: Filename to be read.")
	print("2nd Argument: Flename to be written.")
	exit()
	
fread  = open(filename_read, "rb")
fwrite = open(filename_write, "wb")

state = "START"
counter = 0

try:
	byte_str = fread.read(1)
	while byte_str != "":
	
		byte_int = ord(byte_str)
		byte_hex = hex(byte_int)
		
		if state == "START":
			if byte_hex == '0xff': state = "FF"
			else: state = "START"
		elif state == "FF":
			if   byte_hex == '0xff': state = "FF"
			elif byte_hex == '0xd8': state = "DONE"
			else: state = "START"
		elif state == "DONE":
			counter += 1
			if counter == 3:
				fwrite.write(chr(int('ff', 16)))
				fwrite.write(chr(int('d8', 16)))
				fwrite.write(byte_str)
				state = "FINAL"
			else:
				if byte_hex == '0xff': state = "FF"
				else: state = "START"
		elif state == "FINAL":
			fwrite.write(byte_str)
		
		byte_str = fread.read(1)
		
finally:
	fread.close()
	fwrite.close()
