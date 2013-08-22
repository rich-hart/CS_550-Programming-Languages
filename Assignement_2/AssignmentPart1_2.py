# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
import os
from ListExt import *
from programext import *
sys.path.insert(0,"../..")

if sys.version_info[0] >= 3:
    raw_input = input

tokens = ('NUMBER','LBRACKET','RBRACKET','COMMA')

t_LBRACKET	= r'\['
t_RBRACKET	= r'\]'
t_COMMA	= r'\,'
t_NUMBER = r'[0-9]+'
# Tokens
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules



def p_list(p):
	'''list : LBRACKET sequence RBRACKET
			| LBRACKET RBRACKET'''
	if len( p ) == 4:
		p[0] =p[2]
	else:
		p[0] = []

def p_sequence(p):
	'''sequence : listelement COMMA sequence
				| listelement'''
	
	if len( p ) ==2:
		p[0] = [p[1]]
	else:
		p[3].insert( 0,p[1])
		p[0] = p[3]
		

def p_listelement(p):
	'''listelement : list
				   | NUMBER'''
	p[0] = p[1]

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

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