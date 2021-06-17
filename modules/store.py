from modules.customer import Customer
from modules.inventory import Inventory

class Store:
    
    def __init__(self, name):  # Name is expected to be name of store
        self.name = name
#        everybody = Customer()

        # Load customer file
    #    print(Customer.load_customers())
        Customer.load_customers()

        # Load inventory file
        Inventory.load_inventory()    
