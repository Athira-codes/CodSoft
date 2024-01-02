# ###to_do_list creation
#
# to_do_list = []
# print("ADD_TASK=1")
# print("REMOVE_TASK=2")
# print("DISPLAY_TASK=3")
# print("TASk_DONE=4")
# print("EXIT=5")
# while (True):
#     ADD_TASK = 1
#     REMOVE_TASK = 2
#     DISPLAY_TASK = 3
#     TASK_DONE=4
#     EXIT = 5
#     choice = int(input("enter your choice (1-4):"))
#     if (choice == 1):
#         task = input("enter the task:")
#         to_do_list.append(task)
#     elif (choice == 2):
#         try:
#             task_index = int(input("Enter the task number to delete: "))
#             if 1 <= task_index <= len(task):
#                 remove_task = to_do_list.pop(task_index - 1)
#                 print(f"Task", remove_task, "deleted successfully!")
#             else:
#                 print("Invalid task number. Please enter a valid task number.")
#         except ValueError:
#             print("Invalid input. Please enter a valid task number.")
#
#     elif (choice == 3):
#         if (not to_do_list):
#             print("your to_do_list is empty")
#         else:
#             print("to_do_list:-")
#             for task in to_do_list:
#                 print("--->", task)
#     elif(choice==4):
#         try:
#                task_index = int(input("enter the task_number of the completed task : "))
#                if 1 <= task_index <= len(task):
#                     task_done=to_do_list[task_index-1]
#                     print(task_done,"--->DONE")
#                else:
#                    print("Invalid task number. Please enter a valid task number.")
#         except ValueError:
#             print("Invalid input. Please enter a valid task number.")
#     elif (choice == 5):
#         print("Exiting from the to_do_list programme")
#         break
#     else:
#         print("Please input a valid choice(1-4)")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
