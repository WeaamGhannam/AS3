with open("primenumber.txt","r") as file:
      file.read()
#Use a function to check if a number is prime.
def is_prime(num):
  if num > 1:
    for i in range(2,num):
      if (num % i) == 0:
        return False
    return True
  else:
    return False

# Let the user input a range of numbers.

min_limit = int(input("Enter the min limit of the range: "))
max_limit = int(input("Enter the max limit of the range: "))
# error checking 
if max_limit <= min_limit:
  print("The max limit should be greater than the min limit")

# printing primes 

print(f"Numbers that are prime in the range ({min_limit},{max_limit}) are:")
for number in range(min_limit,max_limit+1):
  if is_prime(number):
    print(number,end=" ")
  

file.close()
