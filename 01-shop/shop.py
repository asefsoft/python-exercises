
# Mostafa Asef Agah
# Ez-Shop Project
# 2019/01/06

shopping_list = []


# display user shopping list
def print_shopping_list():

    if not shopping_list:
        print("Your shopping list is empty!\n")
        return

    print("Your shopping list is:")
    print("\n".join(shopping_list))


# add new item to shopping list if it does not exist
def add_item(item):
    if item in shopping_list:
        print("'{}' is already on your shopping list\n".format(item))
    elif item == "":
        print("Please enter valid item name!\n")
    else:
        shopping_list.append(item)
        print("'{}' added to your shopping list\n".format(item))


# display help message
def print_help():
    print("""
********************************************************
        Welcome to Ez-shop.
        Enter your shopping item names here.
        To display your shopping list enter 'SHOW'
        Enter 'HELP' to display this help.
        For finish shopping enter 'DONE'.
********************************************************        
    """)


# project execution starts from here
print_help()

while True:

    user_command = input("Please enter your command:").lower()

    if user_command == "done":
        print_shopping_list()
        print("\nThank you for shopping. Come back soon :)")
        break

    elif user_command == "show":
        print_shopping_list()

    elif user_command == "help":
        print_shopping_list()

    else:
        add_item(user_command)
