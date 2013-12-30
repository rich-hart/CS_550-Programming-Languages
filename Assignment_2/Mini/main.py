#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2013-12-28.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os

from ply import lex
import ply.yacc as yacc

from interpreter import *

lex.lex()
yacc.yacc()

######   MAIN   #################################


def test_parser( arg=sys.argv ) :
	data = sys.stdin.read()
	yacc.parse( data )


if __name__ == '__main__' :
	test_parser()
