#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2013-12-28.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os
import imp



from new_language import * 




def main( arg=sys.argv ) :
	print(tokens)
	input_file_path=os.path.abspath('.')+'/sample_mini.p'
	#input_file_path=os.path.abspath('.')+'/sample_part_1_2.p'
	Input_File = open(input_file_path,'r')
	raw_file = Input_File.read()
	print "raw_file:\n\n " + raw_file
	print "Output:\n\n "
	result = yacc.parse(raw_file)
	print(result)
	

if __name__ == '__main__' :
	main()
