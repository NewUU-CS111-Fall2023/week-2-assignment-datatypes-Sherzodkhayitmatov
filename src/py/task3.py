import random

def generate_100_digit_number():
  """Generates a 100 digit random number."""
  number = ""
  for i in range(100):
    number += str(random.randint(0, 9))
  return number

def divide_long_numbers(number, divisor):
  """Divides two long numbers.

  Args:
    number: The number to be divided.
    divisor: The number to divide by.

  Returns:
    The quotient of the division.
  """
  quotient = ""
  remainder = ""
  for i in range(len(number)):
    remainder += number[i]
    while int(remainder) >= divisor:
      quotient += str(int(remainder) // divisor)
      remainder = str(int(remainder) % divisor)
    remainder = remainder[1:]
  return quotient, remainder


A = int(input("Enter the number A: "))


number = generate_100_digit_number()


quotient, remainder = divide_long_numbers(number, A)


print(f"The result of dividing {number} by {A} is {quotient}, with a remainder of {remainder}.")
