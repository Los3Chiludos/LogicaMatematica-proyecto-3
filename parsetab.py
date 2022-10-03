
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftOORleftANDrightNEGleftIMPleftIMDAND IMD IMP LPR NEG OOR RPR VAR\n    calc : expression\n    expression : expression AND expression\n                  | expression OOR expression\n                  | expression IMP expression\n                  | expression IMD expression\n                  | NEG expression\n                  | LPR expression RPR\n                  | VAR\n    empty :\n    '
    
_lr_action_items = {'NEG':([0,3,4,6,7,8,9,],[3,3,3,3,3,3,3,]),'LPR':([0,3,4,6,7,8,9,],[4,4,4,4,4,4,4,]),'VAR':([0,3,4,6,7,8,9,],[5,5,5,5,5,5,5,]),'$end':([1,2,5,10,12,13,14,15,16,],[0,-1,-8,-6,-2,-3,-4,-5,-7,]),'AND':([2,5,10,11,12,13,14,15,16,],[6,-8,-6,6,-2,6,-4,-5,-7,]),'OOR':([2,5,10,11,12,13,14,15,16,],[7,-8,-6,7,-2,-3,-4,-5,-7,]),'IMP':([2,5,10,11,12,13,14,15,16,],[8,-8,8,8,8,8,-4,-5,-7,]),'IMD':([2,5,10,11,12,13,14,15,16,],[9,-8,9,9,9,9,9,-5,-7,]),'RPR':([5,10,11,12,13,14,15,16,],[-8,-6,16,-2,-3,-4,-5,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'calc':([0,],[1,]),'expression':([0,3,4,6,7,8,9,],[2,10,11,12,13,14,15,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> calc","S'",1,None,None,None),
  ('calc -> expression','calc',1,'p_calc','main.py',63),
  ('expression -> expression AND expression','expression',3,'p_expression','main.py',69),
  ('expression -> expression OOR expression','expression',3,'p_expression','main.py',70),
  ('expression -> expression IMP expression','expression',3,'p_expression','main.py',71),
  ('expression -> expression IMD expression','expression',3,'p_expression','main.py',72),
  ('expression -> NEG expression','expression',2,'p_expression','main.py',73),
  ('expression -> LPR expression RPR','expression',3,'p_expression','main.py',74),
  ('expression -> VAR','expression',1,'p_expression','main.py',75),
  ('empty -> <empty>','empty',0,'p_empty','main.py',93),
]
