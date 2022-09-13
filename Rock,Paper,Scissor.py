"""Rock Paper Scissor GAME"""
import random

opt = ("ROCK", "PAPER", "SCISSOR")
i = 0
user_count = 0
comp_count = 0
name = input("Please Enter your name: ").upper()
print(f"Welcome! {name} Lets Start...")
print("""Press to 
[P] - PLAY
[Q] - QUIT
""")
first = input(": ").upper()
try:
    while i < 5:
        i = i + 1
        print(f"Round {i}")
        if first == "P":
            comp = random.choice(opt)
            print("""Make your choice!
             [R] - ROCK
             [P] - PAPER
             [S] - SCISSOR
             """)
            user = input(": ").upper()
            if user == "R":
                print("You choose {ROCK}")
                print(f"Computer choose {comp}")
                if user == "R" and comp == "SCISSOR" or user == "P" and comp == "ROCK" or user == "S" and comp == "PAPER":
                    print(f"CONGRATULATION!!! {name} You Win")
                    user_count = +1
                elif user == "R" and comp == "ROCK" or user == "S" and comp == "SCISSOR" or user == "P" and comp == "PAPER":
                    print("GAME DRAW!!!")
                else:
                    print(f"BETTER LUCK NEXT TIME!!! {name} You Loose")
                    comp_count = +1
            elif user == "P":
                print("You choose {PAPER}")
                print(f"Computer choose {comp}")
                if user == "R" and comp == "SCISSOR" or user == "P" and comp == "ROCK" or user == "S" and comp == "PAPER":
                    print(f"CONGRATULATION!!! {name} You Win")
                    user_count = +1
                elif user == "R" and comp == "ROCK" or user == "S" and comp == "SCISSOR" or user == "P" and comp == "PAPER":
                    print("GAME DRAW!!!")
                else:
                    print(f"BETTER LUCK NEXT TIME!!! {name} You Loose")
                    comp_count = +1
            elif user == "S":
                print("You choose {SCISSOR}")
                print(f"Computer choose {comp}")
                if user == "R" and comp == "SCISSOR" or user == "P" and comp == "ROCK" or user == "S" and comp == "PAPER":
                    print(f"CONGRATULATION!!! {name} You Win")
                    user_count = +1
                elif user == "R" and comp == "ROCK" or user == "S" and comp == "SCISSOR" or user == "P" and comp == "PAPER":
                    print("GAME DRAW!!!")
                else:
                    print(f"BETTER LUCK NEXT TIME!!! {name} You Loose")
                    comp_count = +1
            else:
                print("Please Enter Valid Alphabet and Try Again")
        elif first == "Q":
            break
        else:
            print("Please Enter Valid Alphabet and Try Again")
            break
except Exception as e:
    print("Error!", e, "Please Enter Valid Alphabet not numbers")
print()
print("Final Result")
print()
print(f"{name} You score | {user_count}")
print(f"Computer score | {comp_count}")
print(f"Total rounds played - {i}")
if user_count > comp_count:
    print(f"CONGRATULATION!!! {name} You are the Winner of this game")
elif user_count == comp_count:
    print("!*!GAME DRAW!*!")
else:
    print(f"BETTER LUCK NEXT TIME!!! {name} You Loose")
