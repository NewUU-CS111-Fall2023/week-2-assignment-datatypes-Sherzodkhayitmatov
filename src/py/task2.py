import random

def generate_random_number(lower_bound=1, upper_bound=100):
  return random.randint(lower_bound, upper_bound)

def play_guessing_game():
 secret_number = generate_random_number()
  guessed_correctly = False
  while not guessed_correctly:
   
    guess = int(input("Enter a guess: "))

    
    if guess == secret_number:
      guessed_correctly = True
    elif guess < secret_number:
      print("Too low!")
    else:
      print("Too high!")

  
  print("Congratulations! You guessed the correct number!")

if __name__ == "__main__":
  play_guessing_game()
