import random

while True:
    input("Press Enter to roll the dice...")
    dice = random.randint(1, 6)
    print("You rolled:", dice)

    choice = input("Roll again? (y/n): ")
    if choice.lower() != 'y':
        break

print("Game Over!")
print("hello")