def memo(fn):
  cache = {}

  def wrapped(*args, **kwargs):
    key_string = str(args)+str(kwargs)
    if key_string not in cache:
      cache[key_string] = fn(*args, **kwargs)
    return cache[key_string]

  return wrapped

@memo
def factorial(n):
  return n * factorial(n-1) if n > 1 else 1

def primes(n):
  """ Returns  a list of primes < n """
  n = int(n)
  sieve = [True] * n
  for i in range(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
  return [2] + [i for i in range(3,n,2) if sieve[i]]

if __name__ == '__main__':
  print(
    primes(10000000)[-1]
  )
