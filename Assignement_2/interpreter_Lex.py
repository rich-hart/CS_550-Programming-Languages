#!/usr/bin/python
#
# exp2.py - Demonstration of a scanner and generator parser in Python
#		See cs550/Lectures/grammars/exp2.{l,y}
#		Uses an unambiguous grammar
#
#	See http://www.dabeaz.com/ply/ply.html for explanations and a similar (but
#	cooler) example.
#
# Kurt Schmidt
# 7/07
#
# EDITOR:  cols=80, tabstop=2
#
# NOTES:
#		the display() method everybody has is just to graphically spit the
#		actual parse tree to the screen
#
#		The grammar can be found in programext.py  (probably should be here)
#
#

import sys
from programext import *
import AssignmentPart1_2 

i_tokens = (
	'PLUS',
	'MINUS',
	'TIMES',
	'LPAREN',
	'RPAREN',
	'SEMICOLON',
	'COMMA',
	'NUMBER',
	'ASSIGNOP',
	'WHILE',
	'DO',
	'OD',
	'IF',
	'THEN',
	'ELSE',
	'FI',
	'DEFINE',
	'PROC',
	'END',
	'IDENT'
)

	# These are all caught in the IDENT rule, typed there.
reserved = {
		'while' : 'WHILE',
		'do'		: 'DO',
		'od'		: 'OD',
		'if'		: 'IF',
		'then'	: 'THEN',
		'else'	: 'ELSE',
		'fi'		: 'FI',
		'define': 'DEFINE',
		'proc'	: 'PROC',
		'end'		: 'END'
		}

# Now, this section.  We have a mapping, REs to token types (please note
# the t_ prefix).  They simply return the type.

	# t_ignore is special, and does just what it says.  Spaces and tabs
t_ignore = ' \t'

	# These are the simple maps
t_PLUS		= r'\+'
t_MINUS   = r'-'
t_TIMES		= r'\*'
t_LPAREN	= r'\('
t_RPAREN	= r'\)'
t_ASSIGNOP = r':='
t_SEMICOLON = r';'
t_COMMA		= r','

def t_IDENT( t ):
	#r'[a-zA-Z_][a-zA-Z_0-9]*'
	r'[a-z]+'
	t.type = reserved.get( t.value, 'IDENT' )    # Check for reserved words
	return t

def t_NUMBER( t ) :
	r'[0-9]+'

		# t.value holds the string that matched.  Dynamic typing - no unions
	t.value = int( t.value )
	return t

	# These are standard little ditties:
def t_newline( t ):
  r'\n+'
  t.lexer.lineno += len( t.value )

  # Error handling rule
def t_error( t ):
  print "Illegal character '%s' on line %d" % ( t.value[0], t.lexer.lineno )
  return t
  #t.lexer.skip( 1 )
