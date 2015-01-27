#! /usr/bin/python

fd = open("/etc/passwd", "r")
lines = fd.readlines()
fd.close()

for line in lines:
	arg_list = line.split(":")
	print arg_list[0] + ":", arg_list[-1]