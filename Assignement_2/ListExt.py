#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by Richard Hart on 2013-08-22.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import sys
import os


class List :
	'''builds/stores a list of Stmts'''

	def __init__( self ) :
		self.sl = []
	
	def insert( self, num ) :
		self.sl.insert( 0, num )
	
	def eval( self, nt, ft ) :
		for s in self.sl :
			s.eval( nt, ft )
	
	def display( self, nt, ft, depth=0 ) :
		print "%sLIST" % (tabstop*depth)
		for s in self.sl :
			s.display( nt, ft, depth + 1 )
