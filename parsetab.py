
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADJECTIVES ADVERBS ARTICLES CONJUNCTIONS DETERMINANT INTERJECTIONS LPAREN NOUNS PREPOSITIONS PRONOUNS PUNCTUATION RPAREN VERBS\n    S : ADVP PUNCTUATION ADVP PUNCTUATION\n      | VP CP PUNCTUATION\n      | ADVP LPAREN INTERJECTIONS NP RPAREN PUNCTUATION\n      | ADVP LPAREN VP RPAREN PUNCTUATION\n      | ADVP PUNCTUATION\n      | VP LPAREN PP RPAREN PUNCTUATION\n      | CP LPAREN CP RPAREN PUNCTUATION\n      | VP VP ADJP LPAREN ADVP RPAREN PUNCTUATION\n      | ADVP VP PP LPAREN ADVP RPAREN PUNCTUATION\n      | VP NP PP PUNCTUATION\n      | VP ADVP ADJP PUNCTUATION \n      | VP LPAREN VP PP RPAREN PUNCTUATION\n      | VP PP ADJP PUNCTUATION\n      | CP VP NP PUNCTUATION\n      | VP VP PUNCTUATION\n      | ADVP PP PUNCTUATION \n      | ADVP LPAREN INTERJECTIONS RPAREN PUNCTUATION\n      | VP LPAREN VP RPAREN PUNCTUATION\n      | ADVP LPAREN INTERJECTIONS NOUNS RPAREN PUNCTUATION\n      | VP VP VP ADJP LPAREN ADVP RPAREN PUNCTUATION\n      | VP CP LPAREN CONJUNCTIONS VP RPAREN PUNCTUATION\n      | VP LPAREN VERBS VERBS PP RPAREN PUNCTUATION\n      | VP LPAREN PP RPAREN \n    \n    ADVP : ADVERBS NOUNS\n         | ADVERBS VERBS\n         | ADVERBS VERBS ADJP\n         | ADVERBS VERBS ADVERBS\n         | ADVERBS VERBS ADVERBS NOUNS\n         | ADVERBS PP\n         | ADVERBS VERBS DETERMINANT VERBS NOUNS  \n    \n    VP : VERBS VERBS ADVERBS\n       | VERBS ADVERBS \n       | PRONOUNS VERBS PRONOUNS\n       | PRONOUNS VERBS\n       | PRONOUNS VERBS VERBS ADVERBS\n       | VERBS PRONOUNS ADVERBS\n       | VERBS ADVERBS VERBS \n       | PRONOUNS VERBS VERBS ADVERBS NOUNS\n       | VERBS ADJECTIVES NOUNS\n       | ARTICLES NOUNS VERBS ADVERBS VERBS  VERBS DETERMINANT  \n       | VERBS NOUNS PP\n       | VERBS ADJECTIVES\n       | VERBS PRONOUNS NOUNS ARTICLES VERBS \n        \n    \n    NP : NOUNS PREPOSITIONS ADJECTIVES\n       | PRONOUNS NOUNS\n       | ARTICLES NOUNS\n       | DETERMINANT NOUNS \n       \n    \n    PP : PREPOSITIONS NP VP \n       | PREPOSITIONS VERBS \n       | PREPOSITIONS ADJP\n       | PREPOSITIONS NP\n       | PREPOSITIONS NOUNS\n       | PREPOSITIONS PRONOUNS PRONOUNS NOUNS\n       | PREPOSITIONS ARTICLES NOUNS PREPOSITIONS NOUNS DETERMINANT\n       | PREPOSITIONS ARTICLES NOUNS\n       | PREPOSITIONS NP ARTICLES VERBS\n    \n    CP : CONJUNCTIONS VP \n       | CONJUNCTIONS CONJUNCTIONS\n       \n    \n    ADJP : DETERMINANT ADJECTIVES NOUNS \n         | ARTICLES ADJECTIVES NOUNS\n         | DETERMINANT ADJECTIVES\n         | PRONOUNS ADJECTIVES NOUNS\n         | NOUNS ADJECTIVES \n    '
    
_lr_action_items = {'ADVERBS':([0,3,6,10,29,30,31,32,35,37,44,45,46,47,62,68,71,76,77,78,80,81,85,86,87,93,94,96,99,101,103,108,112,119,126,127,128,130,131,132,140,142,155,160,],[7,7,30,7,76,-32,78,-42,82,-34,-51,-49,-50,-52,30,-45,-47,-31,-37,-36,-39,-41,-33,119,120,7,-48,-63,-46,-61,7,76,-44,-35,-56,-53,-62,-60,-59,7,-43,-38,-54,-40,]),'VERBS':([0,2,3,4,5,6,7,8,11,14,15,17,21,27,28,30,32,34,35,36,37,38,44,45,46,47,57,62,68,70,71,76,77,78,80,81,82,83,84,85,94,95,96,99,101,104,112,116,117,119,120,126,127,128,130,131,140,141,142,143,155,160,],[6,6,6,6,6,29,35,37,6,45,6,62,37,-58,-57,77,-42,-24,-25,-29,86,87,6,-49,-50,-52,37,108,-45,87,-47,-31,-37,-36,-39,-41,-27,-26,118,-33,-48,126,-63,-46,-61,6,-44,140,-28,-35,143,-56,-53,-62,-60,-59,-43,-30,-38,153,-54,-40,]),'PRONOUNS':([0,2,3,4,5,6,11,14,15,17,18,19,26,27,28,30,32,34,35,36,37,40,44,45,46,47,48,51,62,68,71,76,77,78,80,81,82,83,85,94,96,99,101,104,112,117,119,126,127,128,130,131,140,141,142,155,160,],[8,8,21,8,8,31,8,48,57,8,65,65,74,-58,-57,-32,-42,-24,65,-29,85,74,8,-49,-50,-52,97,65,31,-45,-47,-31,-37,-36,-39,-41,-27,-26,-33,-48,-63,-46,-61,8,-44,-28,-35,-56,-53,-62,-60,-59,-43,-30,-38,-54,-40,]),'ARTICLES':([0,2,3,4,5,11,14,15,17,18,19,26,27,28,30,32,34,35,36,37,40,44,45,46,47,51,68,71,76,77,78,79,80,81,82,83,85,94,96,99,101,104,112,117,119,126,127,128,130,131,140,141,142,155,160,],[9,9,23,9,9,9,49,56,9,64,64,75,-58,-57,-32,-42,-24,64,-29,-34,75,95,-49,-50,-52,64,-45,-47,-31,-37,-36,116,-39,-41,-27,-26,-33,-48,-63,-46,-61,9,-44,-28,-35,-56,-53,-62,-60,-59,-43,-30,-38,-54,-40,]),'CONJUNCTIONS':([0,3,5,25,30,32,37,44,45,46,47,59,68,71,76,77,78,80,81,85,94,96,99,101,112,119,126,127,128,130,131,140,142,155,160,],[5,5,27,5,-32,-42,-34,-51,-49,-50,-52,104,-45,-47,-31,-37,-36,-39,-41,-33,-48,-63,-46,-61,-44,-35,-56,-53,-62,-60,-59,-43,-38,-54,-40,]),'$end':([1,10,43,53,58,88,107,109,110,111,114,122,124,136,137,139,144,145,151,154,157,158,159,161,],[0,-5,-16,-15,-2,-1,-23,-13,-11,-10,-14,-17,-4,-18,-6,-7,-3,-19,-12,-9,-8,-21,-22,-20,]),'PUNCTUATION':([2,13,15,16,27,28,30,32,34,35,36,37,39,44,45,46,47,63,66,67,68,71,73,76,77,78,80,81,82,83,85,90,92,94,96,99,101,106,107,112,113,115,117,119,121,123,126,127,128,130,131,135,140,141,142,146,149,150,152,155,156,160,],[10,43,53,58,-58,-57,-32,-42,-24,-25,-29,-34,88,-51,-49,-50,-52,109,110,111,-45,-47,114,-31,-37,-36,-39,-41,-27,-26,-33,122,124,-48,-63,-46,-61,136,137,-44,139,-46,-28,-35,144,145,-56,-53,-62,-60,-59,151,-43,-30,-38,154,157,158,159,-54,161,-40,]),'LPAREN':([2,3,4,16,27,28,30,32,34,35,36,37,42,44,45,46,47,52,68,71,76,77,78,80,81,82,83,85,94,96,99,101,102,112,117,119,126,127,128,130,131,140,141,142,155,160,],[11,17,25,59,-58,-57,-32,-42,-24,-25,-29,-34,93,-51,-49,-50,-52,103,-45,-47,-31,-37,-36,-39,-41,-27,-26,-33,-48,-63,-46,-61,132,-44,-28,-35,-56,-53,-62,-60,-59,-43,-30,-38,-54,-40,]),'PREPOSITIONS':([2,3,7,12,17,20,22,30,32,33,34,35,36,37,44,45,46,47,60,68,70,71,76,77,78,80,81,82,83,85,91,94,96,99,101,108,112,117,119,126,127,128,130,131,140,141,142,155,160,],[14,14,14,14,14,14,69,-32,-42,14,-24,-25,-29,-34,-51,-49,-50,69,14,-45,-46,-47,-31,-37,-36,-39,-41,-27,-26,-33,69,-48,-63,129,-61,14,-44,-28,-35,-56,-53,-62,-60,-59,-43,-30,-38,-54,-40,]),'NOUNS':([3,6,7,9,14,15,18,19,21,23,24,26,30,31,32,34,35,36,37,40,44,45,46,47,48,49,50,51,56,62,68,71,74,75,76,77,78,80,81,82,83,85,94,95,96,97,98,99,100,101,112,117,118,119,126,127,128,129,130,131,140,141,142,155,160,],[22,33,34,38,47,55,55,55,68,70,71,22,-32,79,80,-24,55,-29,-34,91,-51,-49,-50,-52,68,99,71,55,38,33,-45,-47,68,115,-31,-37,-36,-39,-41,117,-26,-33,-48,38,-63,127,128,-46,130,131,-44,-28,141,142,-56,-53,-62,147,-60,-59,-43,-30,-38,-54,-40,]),'DETERMINANT':([3,14,15,18,19,26,30,32,34,35,36,37,40,44,45,46,47,51,68,71,76,77,78,80,81,82,83,85,94,96,99,101,112,117,119,126,127,128,130,131,140,141,142,147,153,155,160,],[24,50,54,54,54,24,-32,-42,-24,84,-29,-34,24,-51,-49,-50,-52,54,-45,-47,-31,-37,-36,-39,-41,-27,-26,-33,-48,-63,-46,-61,-44,-28,-35,-56,-53,-62,-60,-59,-43,-30,-38,155,160,-54,-40,]),'ADJECTIVES':([6,47,48,49,50,54,55,56,57,62,64,65,69,84,],[32,96,98,100,101,101,96,100,98,32,100,98,112,101,]),'INTERJECTIONS':([11,],[40,]),'RPAREN':([27,28,30,32,34,35,36,37,40,41,44,45,46,47,60,61,68,71,72,76,77,78,80,81,82,83,85,89,91,94,96,99,101,105,112,115,117,119,125,126,127,128,130,131,133,134,138,140,141,142,148,155,160,],[-58,-57,-32,-42,-24,-25,-29,-34,90,92,-51,-49,-50,-52,106,107,-45,-47,113,-31,-37,-36,-39,-41,-27,-26,-33,121,123,-48,-63,-46,-61,135,-44,-46,-28,-35,146,-56,-53,-62,-60,-59,149,150,152,-43,-30,-38,156,-54,-40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,],[1,]),'ADVP':([0,3,10,93,103,132,],[2,19,39,125,133,148,]),'VP':([0,2,3,4,5,11,15,17,44,104,],[3,12,15,26,28,41,51,60,94,134,]),'CP':([0,3,25,],[4,16,72,]),'PP':([2,3,7,12,17,20,33,60,108,],[13,18,36,42,61,67,81,105,138,]),'NP':([3,14,26,40,],[20,44,73,89,]),'ADJP':([14,15,18,19,35,51,],[46,52,63,66,83,102,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> ADVP PUNCTUATION ADVP PUNCTUATION','S',4,'p_S','lex.py',136),
  ('S -> VP CP PUNCTUATION','S',3,'p_S','lex.py',137),
  ('S -> ADVP LPAREN INTERJECTIONS NP RPAREN PUNCTUATION','S',6,'p_S','lex.py',138),
  ('S -> ADVP LPAREN VP RPAREN PUNCTUATION','S',5,'p_S','lex.py',139),
  ('S -> ADVP PUNCTUATION','S',2,'p_S','lex.py',140),
  ('S -> VP LPAREN PP RPAREN PUNCTUATION','S',5,'p_S','lex.py',141),
  ('S -> CP LPAREN CP RPAREN PUNCTUATION','S',5,'p_S','lex.py',142),
  ('S -> VP VP ADJP LPAREN ADVP RPAREN PUNCTUATION','S',7,'p_S','lex.py',143),
  ('S -> ADVP VP PP LPAREN ADVP RPAREN PUNCTUATION','S',7,'p_S','lex.py',144),
  ('S -> VP NP PP PUNCTUATION','S',4,'p_S','lex.py',145),
  ('S -> VP ADVP ADJP PUNCTUATION','S',4,'p_S','lex.py',146),
  ('S -> VP LPAREN VP PP RPAREN PUNCTUATION','S',6,'p_S','lex.py',147),
  ('S -> VP PP ADJP PUNCTUATION','S',4,'p_S','lex.py',148),
  ('S -> CP VP NP PUNCTUATION','S',4,'p_S','lex.py',149),
  ('S -> VP VP PUNCTUATION','S',3,'p_S','lex.py',150),
  ('S -> ADVP PP PUNCTUATION','S',3,'p_S','lex.py',151),
  ('S -> ADVP LPAREN INTERJECTIONS RPAREN PUNCTUATION','S',5,'p_S','lex.py',152),
  ('S -> VP LPAREN VP RPAREN PUNCTUATION','S',5,'p_S','lex.py',153),
  ('S -> ADVP LPAREN INTERJECTIONS NOUNS RPAREN PUNCTUATION','S',6,'p_S','lex.py',154),
  ('S -> VP VP VP ADJP LPAREN ADVP RPAREN PUNCTUATION','S',8,'p_S','lex.py',155),
  ('S -> VP CP LPAREN CONJUNCTIONS VP RPAREN PUNCTUATION','S',7,'p_S','lex.py',156),
  ('S -> VP LPAREN VERBS VERBS PP RPAREN PUNCTUATION','S',7,'p_S','lex.py',157),
  ('S -> VP LPAREN PP RPAREN','S',4,'p_S','lex.py',158),
  ('ADVP -> ADVERBS NOUNS','ADVP',2,'p_ADVP','lex.py',171),
  ('ADVP -> ADVERBS VERBS','ADVP',2,'p_ADVP','lex.py',172),
  ('ADVP -> ADVERBS VERBS ADJP','ADVP',3,'p_ADVP','lex.py',173),
  ('ADVP -> ADVERBS VERBS ADVERBS','ADVP',3,'p_ADVP','lex.py',174),
  ('ADVP -> ADVERBS VERBS ADVERBS NOUNS','ADVP',4,'p_ADVP','lex.py',175),
  ('ADVP -> ADVERBS PP','ADVP',2,'p_ADVP','lex.py',176),
  ('ADVP -> ADVERBS VERBS DETERMINANT VERBS NOUNS','ADVP',5,'p_ADVP','lex.py',177),
  ('VP -> VERBS VERBS ADVERBS','VP',3,'p_VP','lex.py',190),
  ('VP -> VERBS ADVERBS','VP',2,'p_VP','lex.py',191),
  ('VP -> PRONOUNS VERBS PRONOUNS','VP',3,'p_VP','lex.py',192),
  ('VP -> PRONOUNS VERBS','VP',2,'p_VP','lex.py',193),
  ('VP -> PRONOUNS VERBS VERBS ADVERBS','VP',4,'p_VP','lex.py',194),
  ('VP -> VERBS PRONOUNS ADVERBS','VP',3,'p_VP','lex.py',195),
  ('VP -> VERBS ADVERBS VERBS','VP',3,'p_VP','lex.py',196),
  ('VP -> PRONOUNS VERBS VERBS ADVERBS NOUNS','VP',5,'p_VP','lex.py',197),
  ('VP -> VERBS ADJECTIVES NOUNS','VP',3,'p_VP','lex.py',198),
  ('VP -> ARTICLES NOUNS VERBS ADVERBS VERBS VERBS DETERMINANT','VP',7,'p_VP','lex.py',199),
  ('VP -> VERBS NOUNS PP','VP',3,'p_VP','lex.py',200),
  ('VP -> VERBS ADJECTIVES','VP',2,'p_VP','lex.py',201),
  ('VP -> VERBS PRONOUNS NOUNS ARTICLES VERBS','VP',5,'p_VP','lex.py',202),
  ('NP -> NOUNS PREPOSITIONS ADJECTIVES','NP',3,'p_NP','lex.py',209),
  ('NP -> PRONOUNS NOUNS','NP',2,'p_NP','lex.py',210),
  ('NP -> ARTICLES NOUNS','NP',2,'p_NP','lex.py',211),
  ('NP -> DETERMINANT NOUNS','NP',2,'p_NP','lex.py',212),
  ('PP -> PREPOSITIONS NP VP','PP',3,'p_PP','lex.py',219),
  ('PP -> PREPOSITIONS VERBS','PP',2,'p_PP','lex.py',220),
  ('PP -> PREPOSITIONS ADJP','PP',2,'p_PP','lex.py',221),
  ('PP -> PREPOSITIONS NP','PP',2,'p_PP','lex.py',222),
  ('PP -> PREPOSITIONS NOUNS','PP',2,'p_PP','lex.py',223),
  ('PP -> PREPOSITIONS PRONOUNS PRONOUNS NOUNS','PP',4,'p_PP','lex.py',224),
  ('PP -> PREPOSITIONS ARTICLES NOUNS PREPOSITIONS NOUNS DETERMINANT','PP',6,'p_PP','lex.py',225),
  ('PP -> PREPOSITIONS ARTICLES NOUNS','PP',3,'p_PP','lex.py',226),
  ('PP -> PREPOSITIONS NP ARTICLES VERBS','PP',4,'p_PP','lex.py',227),
  ('CP -> CONJUNCTIONS VP','CP',2,'p_CP','lex.py',234),
  ('CP -> CONJUNCTIONS CONJUNCTIONS','CP',2,'p_CP','lex.py',235),
  ('ADJP -> DETERMINANT ADJECTIVES NOUNS','ADJP',3,'p_ADJP','lex.py',242),
  ('ADJP -> ARTICLES ADJECTIVES NOUNS','ADJP',3,'p_ADJP','lex.py',243),
  ('ADJP -> DETERMINANT ADJECTIVES','ADJP',2,'p_ADJP','lex.py',244),
  ('ADJP -> PRONOUNS ADJECTIVES NOUNS','ADJP',3,'p_ADJP','lex.py',245),
  ('ADJP -> NOUNS ADJECTIVES','ADJP',2,'p_ADJP','lex.py',246),
]
