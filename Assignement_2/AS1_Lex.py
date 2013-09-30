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



A_tokens =  ('NUMBER','LBRACKET','RBRACKET','COMMA')


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

