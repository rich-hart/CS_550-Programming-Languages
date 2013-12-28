#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2013-12-28.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os

import ply.lex as lex
import ply.yacc as yacc

from list_parser import *

lex.lex()
yacc.yacc()

import ply.yacc as yacc

def main( arg=sys.argv ) :
	
	input_file_path=os.path.abspath('.')+'/sample.txt'
	if not os.path.isfile(input_file_path):
			input_file_path=os.path.abspath('..')+'/sample.txt'
	Input_File = open(input_file_path,'r')
	raw_file = Input_File.read()
	print "raw_file: " + raw_file
	result = yacc.parse(raw_file)
	print "parsed file: "+ result

if __name__ == '__main__' :
	main()
