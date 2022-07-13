import random

roll = random.randint(0,1)

head_tails = input("Heads or Tails?: ")


if roll == 0 and head_tails.lower() == "heads":
    print(f"The roll is heads and you guessed {head_tails}. You win!")
elif roll == 0 and head_tails.lower() == "tails":
    print(f"The roll is heads and you guessed {head_tails}. You lose!")
elif roll == 1 and head_tails.lower() == "tails":
    print(f"The roll is tails and you guessed {head_tails}. You win!")
elif roll == 1 and head_tails.lower() == "heads":
    print(f"The roll is tails and you guessed {head_tails}. You lose!")
else:
    print("Try again.")
