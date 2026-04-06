def is_prime(number):
    ''''the number take input -- number 
            if number <= 1 --- its not aprime number
            else ckeck for sqrt of the number if it devide by any number in th
              list(from 2 to sqrt(number)) its not a prime number
            else its prime  '''
    if number <= 1:
        return False
    # Check divisibility from 2 to sqrt(number)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


# Simple CLI interaction
def main():

  num = int(input("Enter a number to check if it's prime: "))

  if is_prime(num):
      print(f"{num} is a prime number.")
  else:
      print(f"{num} is not a prime number.")


main()
