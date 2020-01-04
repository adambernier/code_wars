def sum_triangular_numbers(n):
  the_sum = 0
  for i in range(1,n+1):
    the_sum += (i ** 2 + i)//2
  return the_sum
