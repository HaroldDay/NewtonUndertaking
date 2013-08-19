import random
from collections import defaultdict

def generate_board():
  board = []
  for letter in 'ABCDEFGH':
    board.extend(letter+str(i) for i in range(1,4))

  # remove H2
  board.remove('A3')
  board.remove('H3')

  for tile, targets in (
    ('GO',  ['A1']),
    ('JAIL',['C1']),
    ('FP',  ['E1']),
    ('G2J', ['G1']),
    ('T',   ['B1', 'H2']),
    ('R',   ['B1','D1','F1','H1']),
    ('U',   ['C2','F3']),
    ('CC',  ['A2','D2','G3']),
    ('CH',  ['B2','E2','H1']),
  ):
    for idx in (board.index(tile) for tile in targets):
      board.insert(idx, tile)

  return board

def roll(n=6):
  return random.randint(1,n)+random.randint(1,n)

board = generate_board()
curr_pos = 0
counter = defaultdict(int)

community_deck = ['GO','JAIL']+['']*14
random.shuffle(community_deck)

chance_deck = ['GO','JAIL','C1','E3','H2','R1','RN','RN','UN','-3']+['']*6
random.shuffle(chance_deck)

N = int(1E5)
for _ in range(N):
  curr_pos = ( curr_pos+roll(4) ) % len(board)
  tile = board[curr_pos]

  if tile == 'G2J':
    curr_pos = board.index('JAIL')

  elif tile == 'CC':
    target = community_deck.pop()

    if target:
      curr_pos = board.index(target)
    
    community_deck.insert(0, target)

  elif tile == 'CH':
    target = chance_deck.pop()

    if target:
      if target == 'R1':
        curr_pos = (i for i,tile in enumerate(board) if tile == 'R').next()

      elif target == '-3':
        curr_pos -= 3

      elif target == 'RN':
        curr_pos = (i for i, tile in enumerate(board*2) if tile == 'R' and i > curr_pos).next() % len(board)

      elif target == 'UN':
        curr_pos = (i for i, tile in enumerate(board*2) if tile == 'U' and i > curr_pos).next() % len(board)

      else:
        curr_pos = board.index(target)


    chance_deck.insert(0, target)

  counter[curr_pos] += 1

print sorted( (tally*100./N, idx, board[idx]) for idx,tally in counter.iteritems() )[-3:][::-1]