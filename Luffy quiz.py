import time

# Quiz begins
points = 0
print("Are you a REAL fan of One Piece?")
print("YESSSSSSS!!!")
time.sleep(3)

# Question 1
answer = input("Who is Luffy's common name? ").strip().lower()
if answer in ["straw hat luffy", "strawhat luffy"]:
    print("That is correct!!!")
    points += 1
else:
    print("That is incorrect! The correct answer was 'Straw Hat Luffy.'")
print(f"You have {points} points.")
print("Next question!!")
time.sleep(2)

# Question 2
answer = input("What is the bounty of Rookie Rockstar (in numbers)? ").strip().replace(",", "")
if answer in ["94000000", "94 million"]:
    print("That is correct!!!")
    points += 1
else:
    print("That is incorrect! The correct answer was '94,000,000.'")
print(f"You have {points} points.")
print("Next question!!")
time.sleep(2)

# Question 3
answer = input("In Mock Town, how did Bellamy lose to Luffy? ").strip().lower()
if answer == "luffy attacked with one punch and ended bellamy":
    print("That is correct!!!")
    points += 1
else:
    print("That is incorrect! The correct answer was 'Luffy attacked with one punch and ended Bellamy.'")
print(f"You have {points} points.")
print("Last question!!")
time.sleep(2)

# Question 4
answer = input(
    "What flag had to be changed in the manga because of sensitive issues, and what was the issue it was changed over? "
).strip().lower()
if answer == "whitebeard's flag could be mistaken for a swastika":
    print("That is correct!!!")
    points += 1
else:
    print("That is incorrect! The correct answer was 'Whitebeard's flag could be mistaken for a swastika.'")
print(f"You have {points} points.")

# Final message
print(f"Quiz finished! You scored {points} out of 4.")



    
