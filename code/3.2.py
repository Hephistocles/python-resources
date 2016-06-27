import os
end = input("What file type are you interested in?\n")
dirs = os.listdir("/media/christoph/USB DISK/Python")
for d in dirs:
	if (d.endswith(end)):
		print(d)