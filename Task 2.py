# def add(a, b):
#     return (a + b)
#
#
# def sub(a, b):
#     return (a - b)
#
#
# def mult(a, b):
#     return (a * b)
#
#
# def div(a, b):
#     return (a / b)
#
#
# print("SIMPLE CALCULATER")
# print("ADDITION=1")
# print("SUBTRACTION=2")
# print("MULTIPLICATION=3")
# print("DIVISION=4")
# print("EXIT=5")
#
# addition = 1
# subtraction = 2
# multiplication = 3
# division = 4
# exit = 5
# while True:
#     choice = int(input("enter your choice(1-4):"))
#     if (choice in [1, 2, 3, 4]):
#         a = float(input("enter the first number:"))
#         b = float(input("enter the second number:"))
#         if (choice == 1):
#             print(a, "+", b, "=", add(a, b))
#         if (choice == 2):
#             print(a, '-', b, '=', sub(a, b))
#         elif (choice == 3):
#             print(a, '*', b, '=', mult(a, b))
#         elif (choice == 4):
#             if (b == 0):
#                 print("ERROR")
#             else:
#                 print(a, '/', b, '=', div(a, b))
#     elif (choice == 5):
#         print("EXIT")
#         break
#     else:
#         print("please enter a valid choice")
