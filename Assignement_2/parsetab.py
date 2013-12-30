
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xbb\xf5A\xf20\x12\xe7y\x18\xe98)@.\xe1\x0f'
    
_lr_action_items = {'LBRACKET':([0,1,9,],[1,1,1,]),'RBRACKET':([1,3,4,5,6,7,8,10,],[6,8,-5,-6,-2,-4,-1,-3,]),'COMMA':([4,5,6,7,8,],[-5,-6,-2,9,-1,]),'NUMBER':([1,9,],[5,5,]),'$end':([2,6,8,],[0,-2,-1,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'listelement':([1,9,],[7,7,]),'list':([0,1,9,],[2,4,4,]),'sequence':([1,9,],[3,10,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> list","S'",1,None,None,None),
  ('list -> LBRACKET sequence RBRACKET','list',3,'p_list','/Users/richardhart/ProgrammingLangauges/CS_550-Programming-Languages/Assignement_2/AS1_YACC.py',21),
  ('list -> LBRACKET RBRACKET','list',2,'p_list','/Users/richardhart/ProgrammingLangauges/CS_550-Programming-Languages/Assignement_2/AS1_YACC.py',22),
  ('sequence -> listelement COMMA sequence','sequence',3,'p_sequence','/Users/richardhart/ProgrammingLangauges/CS_550-Programming-Languages/Assignement_2/AS1_YACC.py',29),
  ('sequence -> listelement','sequence',1,'p_sequence','/Users/richardhart/ProgrammingLangauges/CS_550-Programming-Languages/Assignement_2/AS1_YACC.py',30),
  ('listelement -> list','listelement',1,'p_listelement','/Users/richardhart/ProgrammingLangauges/CS_550-Programming-Languages/Assignement_2/AS1_YACC.py',40),
  ('listelement -> NUMBER','listelement',1,'p_listelement','/Users/richardhart/ProgrammingLangauges/CS_550-Programming-Languages/Assignement_2/AS1_YACC.py',41),
]
