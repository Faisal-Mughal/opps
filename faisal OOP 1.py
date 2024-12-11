import math

def is_prime(num):
  """Determines if a given number is prime."""

  if num <= 1:
    return False
  elif num <= 3:
    return True
  elif num % 2 == 0 or num % 3 == 0:
    return False

  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6

  return True

while True:
  num = int(input("Enter a num (0 to quit): "))
  if num == 0:
    break

  if is_prime(num):
    print(num, "prime num.")
  else:
    print(num, " not  prime num.")