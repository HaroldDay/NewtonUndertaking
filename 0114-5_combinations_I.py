import toolkit as tk

@tk.memo
def combinations(n, m):
  return sum(combinations(n,i-1) for i in range(m-n+1)) + \
             combinations(n,m-1) if m >= n else 1

def problem114():
  print(combinations(3,50))

def problem115():
  N = 50
  M = N
  while combinations(N,M) < 1E6:
    M += 1
  print(M)

problem114()
problem115()