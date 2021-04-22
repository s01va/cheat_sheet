
def readfile(filename):
	f = open(filename, 'r')

	while True:
		line = f.readline()
		if not line:
			break
		print(line)

	###########################
	

	f.close()


def writefile(filename, message):
	f = open(filename, 'a')	# 'a': append 'w': newly write
	f.write(message + "\n")
	f.close()