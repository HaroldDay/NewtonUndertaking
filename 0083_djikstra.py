import numpy as np

DIRDICT = {
  'L' : ( 0,-1),
  'R' : ( 0, 1),
  'U' : (-1, 0),
  'D' : ( 1, 0),
  'B' : (-1, 0, 0),
  'F' : ( 1, 0, 0),
}

def move(pos,step):
  return tuple(map(sum,zip(pos,step)))

def load_matrix(path):
  matM = []
  with open(path,'rb') as f:
    for line in f:
      matM.append(map(int,line.split(',')))
  return np.array(matM)

def find_path(matM, start=(0,0), goal=None, freedom='LRUD'):
  # set some goals
  if goal is None:
    goal = move(matM.shape,(-1,-1))

  closed_set = set()
  open_set   = set([start])
  came_from = {}

  g_score = {start:0}
  f_score = {start:g_score[start]}

  while open_set:
    pos = sorted(open_set, key=lambda x: f_score[x])[0]

    if pos == goal:
      return reconstruct_path(came_from, goal)

    open_set.remove(pos)
    closed_set.add(pos)
    for neighbor in (move(pos,DIRDICT[d]) for d in freedom):
      if -1 in neighbor or neighbor in closed_set:
        continue

      try:
        tentative_g_score = g_score[pos] + matM[neighbor]
      except IndexError:
        continue

      if neighbor not in open_set or tentative_g_score < g_score[neighbor]:
        came_from[neighbor] = pos
        g_score[neighbor] = tentative_g_score
        f_score[neighbor] = g_score[neighbor]
        if neighbor not in open_set:
          open_set.add(neighbor)

  print 'No results found.'

def reconstruct_path(came_from, current_node):
  path = [current_node]
  
  try:
    prev_node = came_from[current_node]
    path.extend(reconstruct_path(came_from, prev_node))
    return path

  except KeyError:
    return path

matM = load_matrix('0083_matrix.txt')
path = find_path(matM, freedom='LRDU')
print path
if path:
  print sum([matM[pos] for pos in path])