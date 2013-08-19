#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2013-08-01.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.

"""

import sys
import os
import re
import glob
index=-1
input_string = ''#'(3,(43),2)x' #reading this data structure twice will yield the input string again.... i think 
TOKEN = ''
read_sequence=''


def Match_Number(token):
	global read_sequence
	if token.isdigit():
		while TOKEN.isdigit():
			read_sequence=read_sequence+TOKEN
			GetToken()
	else:
		print 'Error expected ' + TOKEN + ' but recieved ' + token

def Match(token):
	global read_sequence
	if token == TOKEN:
		read_sequence=read_sequence+token
		GetToken()
	else:
		print 'Error expected ' + TOKEN + ' but recieved ' + token


def GetToken():
	global index
	global TOKEN
	index = index + 1
	TOKEN = input_string[index]

	
def Comp(e,L):
	M=e+L
	return M


def Reverse(L):
	L_reverse = L[::-1]
	return L_reverse	


def List():
	Match('(')
	if TOKEN != ')':
		seq()
	Match(')')

def seq():
	elt()
	if TOKEN == ',':
		Match(',')
		seq()
		
def elt():
	if TOKEN == '(':
		List()
	else:
		Match_Number(TOKEN)

def main():
	global input_string
	input_file_path=os.path.abspath('.')+'/sample.txt'
	if not os.path.isfile(input_file_path):
			input_file_path=os.path.abspath('..')+'/sample.txt'
	Input_File = open(input_file_path,'r')
	raw_file = Input_File.read()
	deliminated = re.split(' |\t|\n',raw_file)
	for token in deliminated:
		if token is not '':
			input_string=input_string+token
	input_string=input_string+'x'
	token = ''
	print "Input string: "+input_string
	GetToken()
	L=List()
	print "Parsed Sequence: "+ read_sequence

if __name__ == '__main__':
	main()

