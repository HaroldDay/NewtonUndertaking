import csv

''' cards as integers
    clubs = 0-12
    diamonds = 13-25
    hearts = 26-38
    spades = 39-51
'''
str2int = {
  '2':0, '3':1, '4':2, '5':3,
  '6':4, '7':5, '8':6, '9':7,
  'T':8, 'J':9, 'Q':10,'K':11,
  'A':12,

  'C':0, 'D':13,'H':26,'S':39,
}

class Hand(object):
  def __init__(self, card_lst):
    self.card_lst = sorted(map(self._parse, card_lst))
    self.numbers = sorted([c%13 for c in self.card_lst])
    self.suits = [c/13 for c in self.card_lst]

  def __str__(self):
    return "%s" % self.card_lst

  def _parse(self, c):
    return str2int[c[0]]+str2int[c[1]]

  def _same_suit(self):
    return len(set(self.suits))==1

  def _consecutive(self):
    i = 0
    for i in range(len(self.card_lst)-1):
      if self.numbers[i]+1 != self.numbers[i+1]:
        return False
    return "%s" % self.numbers[0]

  def _cluster_by_N(self):
    """ Cluster items into best possible hands
        Takes care of
        [0] High Card
        [1] One Pair
        [2] Two Pairs
        [3] Three of a Kind
    """
    return sorted(
      [(self.numbers.count(n),n) for n in set(self.numbers)])

  def get_hands(self):
    sets = self._cluster_by_N()

    if [2,3] == sorted([p[0] for p in sets]):
      # [7] Full House
      sets.append((7.1, sets[1][1]))
      sets.append((7.0, sets[0][1]))

    if 4 in [p[0] for p in sets]:
      # [8] Four of a Kind
      sets.append((8, sets[-1][1]))

    if self._same_suit() and self._consecutive():
      # [9] Straight Flush
      sets.append((9, int(self._consecutive())))

    if self._same_suit() and self._consecutive() == '8':
      # [10] Royal Flush
      sets.append((10, None))

    if self._same_suit():
      # [6] Flush
      for N in self.numbers:
        sets.append((6,N))

    if self._consecutive():
      # [5] Straight
      sets.append((5,max(self.numbers)))

    return sorted(sets)

def compare_hands(h1,h2):
  while h1:
    c1 = h1.pop()
    c2 = h2.pop()

    if c1[0] > c2[0]:
      return 1

    elif c2[0] > c1[0]:
      return 0

    elif c1[0] == c2[0]:
      if c1[1] > c2[1]:
        return 1

      elif c2[1] > c1[1]:
        return 0

  raise ValueError

counter = 0
with open(__file__[:-2]+"txt",'rb') as f:
  r = csv.reader(f, delimiter=' ')
  for l in r:
    h1 = Hand(l[:5]).get_hands()
    h2 = Hand(l[5:]).get_hands()
    counter += compare_hands(h1,h2)

print counter