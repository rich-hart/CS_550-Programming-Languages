#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2013-12-28.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from ply import lex
import ply.yacc as yacc

from programext import * 

from Mini.interpreter import tokens
mini_tokens = tokens

from Mini.interpreter import reserved
mini_reserved = reserved
#from Mini.interpreter import reserved
#mini_reserved = reserved

from Part_1_2.list_parser import tokens#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2013-12-28.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

from ply import lex
import ply.yacc as yacc

from programext import * 

from Mini.interpreter import tokens
mini_tokens = tokens

from Mini.interpreter import reserved
mini_reserved = reserved
#from Mini.interpreter import reserved
#mini_reserved = reserved

from Part_1_2.list_parser import tokens
Part_1_2_tokens = tokens

#from Mini.interpreter import *
#from Mini.programext import *
from Mini.interpreter import *
from Part_1_2.list_parser import *
#from Part_1_2.list_parser import p_listelement

tokens = mini_tokens + Part_1_2_tokens
reserved=mini_reserved
#reserved=mini_reserved




start_program = 'start_program'

def p_start_program( p ) :
	'''start_program : program
					 | list'''
	pass



start_list = 'start_list'

def p_start_list( p ) :
	'''start_list : list'''
	p[0]=List(p[1])


def p_assn( p ) :
	'assign_stmt : IDENT ASSIGNOP expr'
	p[0] = AssignStmt( p[1], p[3] )

def p_assn_list( p ) :
	'assign_list_stmt : IDENT ASSIGNOP list'
	p[0] = AssignListStmt( p[1], p[3] )

def p_stmt( p ) :
	'''stmt : assign_stmt
				| assign_list_stmt 
				| while_stmt
				| if_stmt
				| define_stmt'''
	p[0] = p[1]
#from Part_1_2.list_parser import *
lex.lex()
yacc.yacc()




