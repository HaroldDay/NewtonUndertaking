''' How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''

import toolkit as tk

@tk.memo
def digit_factorial_sum(n):
  return sum(tk.factorial(int(i)) for i in str(n))

def dfs_chain(n):
  seen = []

  while n not in seen:
    seen.append(n)
    n = digit_factorial_sum(n)

  return seen

def f(chain_length, n_max=1*10**2):

  for i in range(n_max, 0, -1):
    print( dfs_chain(i) )

def main():
  print( f(60, n_max=1*10**3) )

if __name__ == '__main__':
  import cProfile
  # cProfile.run('main()')
  main()