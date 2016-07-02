#!/opt/python3
import base64

value = raw_input("Value: ")

option = raw_input("[Encode / Decode]: ")

if option == "encode":
	print base64.b64encode(value)
elif option == "decode":
	print base64.b64decode(value)
else:
	print "Try again.\n Value: "

