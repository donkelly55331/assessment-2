# This needs serious refactoring!

# There's a bug that i haven't found. When a customer is added, menu selections 2, 3, and 4 that report "Customer not found." The customer is added to customer.csv, so it must be in the customers array. If the program is stopped and restarted, the customer is found OK.



from modules.store import Store
from modules.customer import Customer
from modules.inventory import Inventory

# Establish store name
# Load customers and inventory
store = Store("Code Platoon Video")


# my_input prints <prompt1> (menu, explanation, etc.)
# loops printing <prompt2> accepting input until an integer from <min> to <max> is entered
# prints error message if input not appropriate
# returns '' if <enter> pressed
def my_input(prompt1, prompt2, min, max):
    str = None
    print(prompt1)
    while str == None:
        try:
            str = input(f"\n{prompt2}")
            if str == '':
                return ''
            if not str.isnumeric():
                str = None
            else:
                val = int(str)
        except: 
            pass

        if str == None or not (min <= val and val <= max):
            print(f"Please enter a number from {min} to {max}.")
            str = None
    return str

menu = f"\n\nWelcome to {store.name}\n\nWhat would you like to do?\n\n1. View video inventory\n2. View customer's rented videos\n3. Rent video\n4. Return video\n5. Add new customer\n6. Exit\n"

while True:

    choice = my_input(menu, "Your choice:  ", 1, 6 )

    # View video inventory
    if choice == '1':
        Inventory.view_video_inventory()

    # View customer's rented videos
    elif choice == '2':
        id = my_input('', 'Customer ID:  ', 1, 999999)
        if id != '':
            Customer.view_customer_rentals(id)

    # Rent video        
    elif choice == '3':
        id = my_input('', 'Customer ID:  ', 1, 999999)
        if id != '':
            Customer.rent(id)

    # Return video
    elif choice == '4':
        id = my_input('', 'Customer ID:  ', 1, 999999)
        if id != '':
            Customer.returning(id)

    # Add new customer
    elif choice == '5':
        Customer.add_customer()

    # Exit
    elif choice == '6':
        print("Thanks for visiting\n\n")
        break
