import toolkit as tk

@tk.memo
def combinations(n, m):
  return  combinations(n,m-n) + \
          combinations(n,m-1) if m >= n else 1

@tk.memo
def multinations(ntup, m):
  return sum(multinations(ntup, m-n) for n in ntup if m >= n) + \
             multinations(ntup, m-1) if m != 0 else 1


def problem116():
  print(
    sum(combinations(n, 50) - 1 for n in [2,3,4])
  )

def problem117():
  print(
    multinations((2,3,4), 50)
  )

problem116()
problem117()