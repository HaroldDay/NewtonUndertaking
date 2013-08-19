import itertools

class Network(dict):

  def __init__(self):
    super().__init__()
    self.connected_sets = []

  def __getitem__(self, key):
    return super().__getitem__(tuple(sorted(key)))

  def __setitem__(self, key, value):
    super().__setitem__(tuple(sorted(key)), value)

  def __str__(self):
    return "\n".join(map(str,self.items()))

  def V(self):
    return set(sum(self.keys(),()))

  def E(self):
    return self.values()

  def weight(self):
    return sum(self.values())

  def get_mst(self):
    mst = Network()
    for value, key in sorted((value, key) for key, value in self.items()):
      mst[key] = value
      
      v,w = key
      for s in mst.connected_sets:

        if v in s and w in s:
          del mst[key]
          break

        elif v in s and w not in s:
          s.add(w)

        elif w in s and v not in s:
          s.add(v)

      else:
        mst.connected_sets.append(set(key))
    
      mst.merge_connected_sets()

    return mst

  def merge_connected_sets(self):
    ''' http://stackoverflow.com/questions/9110837/python-simple-list-merging-based-on-intersections '''
    sets = [s for s in self.connected_sets]
    merged = True
    while merged:
      merged = False
      results = []
      while sets:
        common, rest = sets[0], sets[1:]
        sets = []
        for x in rest:
          if x.isdisjoint(common):
            sets.append(x)
          else:
            merged = True
            common |= x
        results.append(common)
      sets = results
    self.connected_sets = sets

  def from_file(self, path):
    with open(path, 'r') as f:

      for i, line in enumerate(f):
        for j, c in enumerate(str(line).strip().split(',')):
          
          try:
            self[(i,j)] = int(c)

          except ValueError:
            pass

def main():
  n = Network()
  n.from_file('0107_network.txt')
  print(n.weight() - n.get_mst().weight())

if __name__ == '__main__':
  main()