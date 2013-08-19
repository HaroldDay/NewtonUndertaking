import toolkit as tk

def n_mult(n, lvl=0):
  for i in range(1,n-2):
    print '\t'*lvl, n-i, i

    map(lambda x: n_mult(x, lvl+1),(n-i, i))
  

def problem122():
  print(
    n_mult(5)
  )

problem122()