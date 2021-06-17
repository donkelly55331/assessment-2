import csv
import os

class Inventory():

    inventory = []

    # read inventory from csv into Inventory.inventory
    @classmethod
    def load_inventory(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")
        with open(path, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for movie in reader:
                cls.inventory.append(movie)
        return

    # update inventory file
    @classmethod
    def update_inventory(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")
        with open(path, 'w', newline = '\n') as csvfile:
            field_names = ['id', 'title', 'rating', 'copies_available']
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
            for item in cls.inventory:
                writer.writerow(item)

    @classmethod
    def view_video_inventory(cls):
        print("\n   ID  Movie Name                    Rating  Available\n")
        for item in cls.inventory:
            print('{:>5}  {:<30}{:<8}{:>6}'.format(item['id'], item['title'], item['rating'], item['copies_available']))
            