def f(n,b = 2):
  l = []
  m = n
  while m:
    l += [m % b]
    m //= b
  return l == l[::-1] and b or f(n, b + 1)
