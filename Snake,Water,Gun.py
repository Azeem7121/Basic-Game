"""SNAKE WATER GUN GAME"""
import random

opt = ("SNAKE", "WATER", "GUN")
i = 0
user_count = 0
comp_count = 0
name = input("Please Enter your name: ").upper()
print("""Press to 
[P] - PLAY
[Q] - QUIT
""")
first = input(": ").upper()
print(f"Welcome! {name} Lets Start...")
try:
    while i < 10:
        i = i + 1
        if first == "P":
            comp = random.choice(opt)
            print("""Make your choice!
             [S] - Snake
             [W] - Water
             [G] - Gun
             """)
            user = input(": ").upper()
            if user == "S":
                print("You choose {Snake}")
                print(f"Computer choose {comp}")
                if user == "S" and comp == "WATER" or user == "W" and comp == "GUN" or user == "G" and comp == "SNAKE":
                    print(f"CONGRATULATION!!! {name} You Win")
                    user_count = +1
                elif user == "S" and comp == "SNAKE" or user == "W" and comp == "WATER" or user == "G" and comp == "GUN":
                    print("GAME DRAW!!!")
                else:
                    print(f"BETTER LUCK NEXT TIME!!! {name} You Loose")
                    comp_count = +1
            elif user == "W":
                print("You choose {WATER}")
                print(f"Computer choose {comp}")
                if user == "S" and comp == "WATER" or user == "W" and comp == "GUN" or user == "G" and comp == "SNAKE":
                    print(f"CONGRATULATION!!! {name} You Win")
                    user_count = +1
                elif user == "S" and comp == "SNAKE" or user == "W" and comp == "WATER" or user == "G" and comp == "GUN":
                    print("GAME DRAW!!!")
                else:
                    print(f"BETTER LUCK NEXT TIME!!! {name} You Loose")
                    comp_count = +1
            elif user == "G":
                print("You choose {GUN}")
                print(f"Computer choose {comp}")
                if user == "S" and comp == "WATER" or user == "W" and comp == "GUN" or user == "G" and comp == "SNAKE":
                    print(f"CONGRATULATION!!! {name} You Win")
                    user_count = +1
                elif user == "S" and comp == "SNAKE" or user == "W" and comp == "WATER" or user == "G" and comp == "GUN":
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
