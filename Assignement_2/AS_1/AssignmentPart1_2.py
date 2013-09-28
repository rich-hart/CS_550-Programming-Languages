# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
import os
#from ListExt import *
sys.path.insert(0,"../..")


from AS1_Lex import *

tokens = A_tokens


# Build the lexer
import ply.lex as lex
lex.lex()

from AS1_YACC import *

import ply.yacc as yacc
yacc.yacc()

def main( arg=sys.argv ) :
	input_file_path=os.path.abspath('.')+'/sample.txt'
	if not os.path.isfile(input_file_path):
			input_file_path=os.path.abspath('..')+'/sample.txt'
	Input_File = open(input_file_path,'r')
	raw_file = Input_File.read()
	print "raw_file: " + raw_file
	result = yacc.parse(raw_file)
	print result

if __name__ == '__main__' :
	main()