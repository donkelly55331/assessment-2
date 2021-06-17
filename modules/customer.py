import csv
import os
from modules.inventory import Inventory

class Customer:

    customers = [] # class variable--list of all customers

    @classmethod
    def load_customers(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for customer in reader:
                cls.customers.append(customer)
        return

    # update customer file
    @classmethod
    def update_customers(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path, 'w', newline = '\n') as csvfile:
            field_names = ['id', 'first_name', 'last_name', 'rentals']
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            for customer in cls.customers:
                writer.writerow(customer)

    # Print customer name and number of movies checked out
    # Print list of movies checked out, if any
    @classmethod
    def view_customer_rentals(cls, customer_id):
        customer = Customer.find_customer_by_id(customer_id)
        if customer == None:
            print('\nCustomer not found\n')
            return       
        movies = customer['rentals'].split('/')
        n = len(movies) if len(movies[0]) > 0 else 0
        print(f"\n{customer['first_name']} {customer['last_name']} has {n if n > 0 else 'no'} movie{'s' if n != 1 else ''} checked out")
        for movie in movies:
            print("   ", movie)           

    def find_customer_by_id(customer_id):
        for customer in Customer.customers:
           if customer['id'] == customer_id:
               return customer

    # Find highest customer number in use and increment
    @classmethod
    def next_id(cls):
        id = -1
        for customer in Customer.customers:
            if int(customer['id']) > id:
                id = int(customer['id'])
        id += 1
        return id     
        
    # Add a customer
    @classmethod
    def add_customer(cls):
        first = input("First name:  ")
        if first == '':
            return
        last = input("Last name:  ")
        if last == '':
            return
        id = Customer.next_id()
        Customer.customers.append({'id': id, 'first_name': first, 'last_name': last})
        Customer.update_customers()

    # Rent a video to a customer
    @classmethod
    def rent(cls, customer_id):
        cust_index = -1
        for i, customer in enumerate(Customer.customers):
            if customer['id'] == customer_id:
                cust_index = i
                break
        if cust_index < 0:
            print('\nCustomer not found\n')
            return       
        if customer['rentals'] == None:
            n = 0
            movies = []
        else:
            movies = customer['rentals'].split('/')
            n = len(movies) if len(movies[0]) > 0 else 0
        if n >= 3:
             print(f"\n{customer['first_name']} {customer['last_name']} already has {n} movies checked out")
             return
        title = input("Movie title:  ")
        if title in movies:
            print(f"\n{customer['first_name']} {customer['last_name']} already has {title} checked out")
            return
        movie_index = -1
        for i,movie in enumerate(Inventory.inventory):
            if movie['title'] == title:
                movie_index = i
                if int(movie['copies_available']) < 1:
                    print(f"{title} is not available")
                    return
        if movie_index < 0:
            print(f"\n{title} does not exist")
            return

        # Movie is available, customer has less than 3, do the deal  
        # Add title to customer's list
        if n == 0:
            Customer.customers[cust_index]['rentals'] = title
        else:
            Customer.customers[cust_index]['rentals'] = Customer.customers[cust_index]['rentals'] + "/" + title

        # Subtract one from available copies
        Inventory.inventory[movie_index]['copies_available'] = int(Inventory.inventory[movie_index]['copies_available']) - 1

        Customer.update_customers()
        Inventory.update_inventory()

    # Return a video

    # This does not handle differences in spelling between customers and inventory, e.g. "Guardians Of The Galaxy" vs. "Guardians of the Galaxy"

    @classmethod
    def returning(cls, customer_id):
        cust_index = -1
        for i, customer in enumerate(Customer.customers):
            if customer['id'] == customer_id:
                cust_index = i
                break
        if cust_index < 0:
            print('\nCustomer not found\n')
            return       
        if customer['rentals'] == None:
            n = 0
            movies = []
        else:
            movies = customer['rentals'].split('/')
            n = len(movies) if len(movies[0]) > 0 else 0
        if n == 0:
             print(f"\n{customer['first_name']} {customer['last_name']} has no movies checked out")
             return
        title = input("Movie title:  ")
        if title not in movies:
            print(f"\n{customer['first_name']} {customer['last_name']} does not have {title} checked out")
            return
        movie_index = -1
        for i,movie in enumerate(Inventory.inventory):
            if movie['title'] == title:
                movie_index = i
        if movie_index < 0:
            print(f"\n{title} does not exist in inventory")
            return

        # Movie is in customer list, found it in inventory, do the deal  
        # Remove title from customer's list
        movies.remove(title)

        # Customer has zero, one, or two movies checked out
        n = len(movies)
        if n == 0:
            Customer.customers[cust_index]['rentals'] = ''
        elif n == 1:
            Customer.customers[cust_index]['rentals'] = movies[0]
        else:
            Customer.customers[cust_index]['rentals'] = movies[0] + "/" + movies[1]

        # Add one to available copies
        Inventory.inventory[movie_index]['copies_available'] = int(Inventory.inventory[movie_index]['copies_available']) + 1

        Customer.update_customers()
        Inventory.update_inventory()
