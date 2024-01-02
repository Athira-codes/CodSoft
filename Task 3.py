# import random
#
# try:
#     length = int(input("enter the length of the password you want(select 4 or above ):"))
#     if (length >= 4):
#         upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         lower = "abcdefghijklmnopqrstuvwxyz"
#         num = "123456789"
#         symbol = "!@#$%^&*.+-~|<>"
#         all = upper + lower + num + symbol
#         a = random.choice(upper)
#         b = random.choice(lower)
#         c = random.choice(symbol)
#         d = random.choice(num)
#         password = a + b + c + d
#         print("PASSWORD:-")
#         for i in range(length - 4):
#             password += random.choice(all)
#         random.shuffle(list(password))
#         print(''.join(password), end="")
#         print("\nTHANKYOU FOR USING PASSWORD GENERATOR!!!")
#     else:
#         print("Invalid number. Please enter a valid length.")
# except ValueError:
#     print("Invalid input. Please enter a valid input.")
