
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x82\x85V\xa1\xba\xe8;^\xb2\xa1znk\x07\xda^'
    
_lr_action_items = {'THEN':([12,13,14,16,18,22,33,37,38,39,42,],[-12,-17,-18,-16,-14,32,-13,-8,-9,-15,-25,]),'ASSIGNOP':([6,],[20,]),'IDENT':([0,1,5,8,17,20,21,23,24,25,26,27,32,40,43,47,49,50,],[6,13,19,13,13,13,6,13,13,6,13,13,6,45,13,6,45,6,]),'END':([2,3,7,10,11,12,13,14,16,18,30,31,33,37,38,39,42,44,53,54,55,],[-7,-4,-3,-6,-5,-12,-17,-18,-16,-14,-19,-2,-13,-8,-9,-15,-25,-20,55,-21,-22,]),'PROC':([19,],[29,]),'SEMICOLON':([2,3,7,10,11,12,13,14,16,18,30,33,37,38,39,42,44,54,55,],[-7,-4,21,-6,-5,-12,-17,-18,-16,-14,-19,-13,-8,-9,-15,-25,-20,-21,-22,]),'DO':([12,13,14,15,16,18,33,37,38,39,42,],[-12,-17,-18,25,-16,-14,-13,-8,-9,-15,-25,]),'RPAREN':([12,13,14,16,18,28,33,34,35,37,38,39,42,45,46,48,52,],[-12,-17,-18,-16,-14,39,-13,42,-11,-8,-9,-15,-25,-24,50,-10,-23,]),'OD':([2,3,7,10,11,12,13,14,16,18,30,31,33,36,37,38,39,42,44,54,55,],[-7,-4,-3,-6,-5,-12,-17,-18,-16,-14,-19,-2,-13,44,-8,-9,-15,-25,-20,-21,-22,]),'NUMBER':([1,8,17,20,23,24,26,27,43,],[16,16,16,16,16,16,16,16,16,]),'ELSE':([2,3,7,10,11,12,13,14,16,18,30,31,33,37,38,39,41,42,44,54,55,],[-7,-4,-3,-6,-5,-12,-17,-18,-16,-14,-19,-2,-13,-8,-9,-15,47,-25,-20,-21,-22,]),'WHILE':([0,21,25,32,47,50,],[1,1,1,1,1,1,]),'PLUS':([12,13,14,15,16,18,22,28,30,33,35,37,38,39,42,],[-12,-17,-18,26,-16,-14,26,26,26,-13,26,-8,-9,-15,-25,]),'LPAREN':([1,8,13,17,20,23,24,26,27,29,43,],[17,17,24,17,17,17,17,17,17,40,17,]),'TIMES':([12,13,14,16,18,33,37,38,39,42,],[23,-17,-18,-16,-14,-13,23,23,-15,-25,]),'FI':([2,3,7,10,11,12,13,14,16,18,30,31,33,37,38,39,42,44,51,54,55,],[-7,-4,-3,-6,-5,-12,-17,-18,-16,-14,-19,-2,-13,-8,-9,-15,-25,-20,54,-21,-22,]),'DEFINE':([0,21,25,32,47,50,],[5,5,5,5,5,5,]),'MINUS':([12,13,14,15,16,18,22,28,30,33,35,37,38,39,42,],[-12,-17,-18,27,-16,-14,27,27,27,-13,27,-8,-9,-15,-25,]),'$end':([2,3,4,7,9,10,11,12,13,14,16,18,30,31,33,37,38,39,42,44,54,55,],[-7,-4,0,-3,-1,-6,-5,-12,-17,-18,-16,-14,-19,-2,-13,-8,-9,-15,-25,-20,-21,-22,]),'COMMA':([12,13,14,16,18,33,35,37,38,39,42,45,],[-12,-17,-18,-16,-14,-13,43,-8,-9,-15,-25,49,]),'IF':([0,21,25,32,47,50,],[8,8,8,8,8,8,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'stmt_list':([0,21,25,32,47,50,],[9,31,36,41,51,53,]),'func_call':([1,8,17,20,23,24,26,27,43,],[14,14,14,14,14,14,14,14,14,]),'term':([1,8,17,20,24,26,27,43,],[12,12,12,12,12,37,38,12,]),'if_stmt':([0,21,25,32,47,50,],[10,10,10,10,10,10,]),'param_list':([40,49,],[46,52,]),'expr':([1,8,17,20,24,43,],[15,22,28,30,35,35,]),'define_stmt':([0,21,25,32,47,50,],[2,2,2,2,2,2,]),'stmt':([0,21,25,32,47,50,],[7,7,7,7,7,7,]),'assign_stmt':([0,21,25,32,47,50,],[3,3,3,3,3,3,]),'while_stmt':([0,21,25,32,47,50,],[11,11,11,11,11,11,]),'program':([0,],[4,]),'expr_list':([24,43,],[34,48,]),'fact':([1,8,17,20,23,24,26,27,43,],[18,18,18,18,33,18,18,18,18,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> stmt_list','program',1,'p_program','interpreter.py',122),
  ('stmt_list -> stmt SEMICOLON stmt_list','stmt_list',3,'p_stmt_list','interpreter.py',130),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list','interpreter.py',131),
  ('stmt -> assign_stmt','stmt',1,'p_stmt','interpreter.py',140),
  ('stmt -> while_stmt','stmt',1,'p_stmt','interpreter.py',141),
  ('stmt -> if_stmt','stmt',1,'p_stmt','interpreter.py',142),
  ('stmt -> define_stmt','stmt',1,'p_stmt','interpreter.py',143),
  ('expr -> expr PLUS term','expr',3,'p_add','interpreter.py',147),
  ('expr -> expr MINUS term','expr',3,'p_sub','interpreter.py',151),
  ('expr_list -> expr COMMA expr_list','expr_list',3,'p_expr_list','interpreter.py',155),
  ('expr_list -> expr','expr_list',1,'p_expr_list','interpreter.py',156),
  ('expr -> term','expr',1,'p_expr_term','interpreter.py',164),
  ('term -> term TIMES fact','term',3,'p_mult','interpreter.py',168),
  ('term -> fact','term',1,'p_term_fact','interpreter.py',172),
  ('fact -> LPAREN expr RPAREN','fact',3,'p_fact_expr','interpreter.py',176),
  ('fact -> NUMBER','fact',1,'p_fact_NUM','interpreter.py',180),
  ('fact -> IDENT','fact',1,'p_fact_IDENT','interpreter.py',184),
  ('fact -> func_call','fact',1,'p_fact_funcall','interpreter.py',188),
  ('assign_stmt -> IDENT ASSIGNOP expr','assign_stmt',3,'p_assn','interpreter.py',192),
  ('while_stmt -> WHILE expr DO stmt_list OD','while_stmt',5,'p_while','interpreter.py',196),
  ('if_stmt -> IF expr THEN stmt_list ELSE stmt_list FI','if_stmt',7,'p_if','interpreter.py',200),
  ('define_stmt -> DEFINE IDENT PROC LPAREN param_list RPAREN stmt_list END','define_stmt',8,'p_def','interpreter.py',204),
  ('param_list -> IDENT COMMA param_list','param_list',3,'p_param_list','interpreter.py',208),
  ('param_list -> IDENT','param_list',1,'p_param_list','interpreter.py',209),
  ('func_call -> IDENT LPAREN expr_list RPAREN','func_call',4,'p_func_call','interpreter.py',217),
]