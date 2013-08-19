''' The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
    and concatenating them in any order the result will always be prime. For
    example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these
    four primes, 792, represents the lowest sum for a set of four primes with
    this property.

    Find the lowest sum for a set of five primes for which any two primes
    concatenate to produce another prime.
'''
import toolkit as tk
import itertools as it

primes = tk.primes(1E6)

@tk.memo
def f(pair):
  a = int(''.join(map(str,pair))) in primes
  b = int(''.join(map(str,pair[::-1]))) in primes
  return a and b

for pair in it.permutations(primes, 2):
  print( pair )
  if f(pair):
    print( pair )
    break