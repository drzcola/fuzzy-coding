#!/opt/python3
import base64

value = raw_input("Value: ")

option = raw_input("[Encode / Decode]: ")

if option == "encode":
	print (value).encode('rot13')
elif option == "decode":
	print (value).decode('rot13')
else:
	print "Try again.\n Value: "

