# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables.   This is from O'Reilly's
# "Lex and Yacc", p. 63.
# -----------------------------------------------------------------------------

import sys
import os
#from ListExt import *
#from programext import *
sys.path.insert(0,"../..")







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

