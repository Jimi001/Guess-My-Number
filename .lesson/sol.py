# See the Instructions tab
import random
# Set secret number
number = random.randint(1,100)
print(number)
print("I'm thinking of a number between 1 and 99")
while True:
  guess = int(input("Enter your guess: "))
  # Ask the user to guess
  
  # Check to see if the guess is <, >, or = secret number
  
  if guess > number:
    print("Too high")
    continue
  elif guess < number:
    print("Too low")
    continue
  elif guess == number:
    print("Congrats! The number is", number)
    break
# Print the right message