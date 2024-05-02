import random

# Set secret number
secret_number = random.randint(1, 99)

print("I'm thinking of a number between 1 and 99")

while True:
  # Ask the user to guess
  guess = input("Enter a guess: ")

  # Check if the input is a number
  if not guess.isdecimal():
    print("Please enter a valid number.")
    continue

  # Convert the input to an integer
  guess = int(guess)

  # Check to see if the guess is <, >, or = secret number
  if guess < secret_number:
    print("Your guess is too low")
  elif guess > secret_number:
    print("Your guess is too high")
  else:
    print(f"Congrats! The number was {secret_number}")
    break
