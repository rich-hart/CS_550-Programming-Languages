#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2013-12-28.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""




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





def p_list(p):
	'''list : LBRACKET sequence RBRACKET
			| LBRACKET RBRACKET'''
	if p[2] == ']':
		p[0] = p[1] + p[2] 
	else:
		p[0] = "[" + p[2] + "]" 

def p_sequence(p):
	'''sequence : listelement COMMA sequence
				| listelement'''
	if len(p) > 2:
		p[0] = p[1] + "," + p[3]
	else:
		p[0] = p[1]

def p_listelement(p):
	'''listelement : list
				   | NUMBER'''
	p[0] = p[1]

def p_error(p):
    if p:
        print("List Grammer: Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

