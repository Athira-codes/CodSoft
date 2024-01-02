# import random
#
#

# def main():
#     l = ["rock", "paper", "scissors"]
#     round = int(input("how many round you want to play:"))
#     user_point = 0
#     computer_point = 0
#     for i in range(round):
#         user = input("choose one from(rock,paper,scissors):")
#         if (user in l):
#             print("\nusers_choice:", user)
#             computer = random.choice(l)
#             print("computers_choice:", computer)
#             if (user == computer):
#                 user_point += 0
#                 computer_point += 0
#                 print("\nuser:", user_point)
#                 print("computer:", computer_point)
#             elif (user == "rock"):
#                 if (computer == "paper"):
#                     print("paper beats rock")
#                     computer_point += 1
#                     print("\nuser:", user_point)
#                     print("computer:", computer_point)
#                 else:
#                     print("rock beats scissor")
#                     user_point += 1
#                     print("\nuser:", user_point)
#                     print("computer:", computer_point)
#
#             elif (user == "paper"):
#                 if (computer == "rock"):
#                     print("paper beats rock")
#                     user_point += 1
#                     print("\nuser:", user_point)
#                     print("computer:", computer_point)
#                 else:
#                     print("scissor beats paper")
#                     computer_point += 1
#                     print("\nuser:", user_point)
#                     print("computer:", computer_point)
#             elif (user == "scissors"):
#                 if (computer == "rock"):
#                     print("rock beats scissors")
#                     computer_point += 1
#                     print("\nuser:", user_point)
#                     print("computer:", computer_point)
#                 else:
#                     user_point += 1
#                     print("\nuser:", user_point)
#                     print("computer:", computer_point)
#
#
#         else:
#             print("enter a valid input")
#     if (user_point > computer_point):
#         print("\nResult:user wins!!")
#     elif (user_point == computer_point):
#         print("\nResult:DRAW")
#     else:
#         print("\nResult:computer wins!!")
#

#
# if __name__ == "__main__":
#     repeat_condition = True
#     while repeat_condition:
#         main()
#         repeat_condition = input("want to play again(YES/NO):").lower() == 'yes'
#         print("Exiting From The Game.....")
