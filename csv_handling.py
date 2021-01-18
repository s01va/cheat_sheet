# -*- coding: utf-8 -*-

import csv

def readcsv():
	f = open(filename, 'r', newline='')
	reader = csv.reader(f, delimiter=',')

	for line in reader:
		if not line:
			break
		# line = [ , , , ] 리스트 형태

	f.close()
	return

def writecsv():
	f = open(filename, 'a', newline='')
	writer = csv.writer(f, delimiter=',')
	writer.writerow(["for", "example", "hello", "world"])
	f.close()
	return