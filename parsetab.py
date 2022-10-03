
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND IMD IMP LPR NEG OOR RPR VARexpression : expression AND expression\n                  | expression OOR expression\n                  | expression IMP expression\n                  | expression IMD expression\n                  | NEG expression\n                  | LPR expression RPR\n                  | VAR\n    empty :\n    '
    
_lr_action_items = {'NEG':([0,2,3,5,6,7,8,],[2,2,2,2,2,2,2,]),'LPR':([0,2,3,5,6,7,8,],[3,3,3,3,3,3,3,]),'VAR':([0,2,3,5,6,7,8,],[4,4,4,4,4,4,4,]),'$end':([1,4,9,11,12,13,14,15,],[0,-7,-5,-1,-2,-3,-4,-6,]),'AND':([1,4,9,10,11,12,13,14,15,],[5,-7,5,5,5,5,5,5,-6,]),'OOR':([1,4,9,10,11,12,13,14,15,],[6,-7,6,6,6,6,6,6,-6,]),'IMP':([1,4,9,10,11,12,13,14,15,],[7,-7,7,7,7,7,7,7,-6,]),'IMD':([1,4,9,10,11,12,13,14,15,],[8,-7,8,8,8,8,8,8,-6,]),'RPR':([4,9,10,11,12,13,14,15,],[-7,-5,15,-1,-2,-3,-4,-6,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,5,6,7,8,],[1,9,10,11,12,13,14,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression AND expression','expression',3,'p_expression','main.py',52),
  ('expression -> expression OOR expression','expression',3,'p_expression','main.py',53),
  ('expression -> expression IMP expression','expression',3,'p_expression','main.py',54),
  ('expression -> expression IMD expression','expression',3,'p_expression','main.py',55),
  ('expression -> NEG expression','expression',2,'p_expression','main.py',56),
  ('expression -> LPR expression RPR','expression',3,'p_expression','main.py',57),
  ('expression -> VAR','expression',1,'p_expression','main.py',58),
  ('empty -> <empty>','empty',0,'p_empty','main.py',66),
]