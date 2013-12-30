#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2013-12-28.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""


#class Element:
class Expr :
	'''Virtual base class for expressions in the language'''

	def __init__( self ) :
		raise NotImplementedError(
			'Expr: pure virtual base class.  Do not instantiate' )

	def eval( self, nt, ft ) :
		'''Given an environment and a function table, evaluates the expression,
		returns the value of the expression (an int in this grammar)'''

		raise NotImplementedError(
			'Expr.eval: virtual method.  Must be overridden.' )

	def display( self, nt, ft, depth=0 ) :
		'For debugging.'
		raise NotImplementedError(
			'Expr.display: virtual method.  Must be overridden.' )

class List(Expr) :
	'''builds/stores a list of Stmts'''

	def __init__( self, list_string ) :
		self.sl = list_string
	
	
	def display( self, nt, ft, depth=0 ) :
		print "%sSTMT LIST" % (tabstop*depth)
		for s in self.sl :
			s.display( nt, ft, depth+1 )
#class Integer:
