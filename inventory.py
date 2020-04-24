""" A class to manage overall inventory """
from product import Product


class Inventory:
    """ Inventory class"""
    def __init__(self):
        self.inventory = {}

    def create_product(self, product_details):
        """ Createa a new product - will check if product already exists"""
        name, price, prod_id, quantity = product_details
        new_product = Product(name, price, prod_id, quantity)
        # Check if product id already exists
        if new_product.prod_id in self.inventory:
            print(f"Product ID {self.inventory[new_product.prod_id].prod_id} "
                  f"already exists with the following details: ")
            print(f"Name: {self.inventory[new_product.prod_id].name}")
            print(f"Price: {self.inventory[new_product.prod_id].price}")
            print(f"Quantity: {self.inventory[new_product.prod_id].quantity}")
            overwrite = input("Do you wish to overwrite? (y/n)")
            if overwrite.lower() == "y":
                self.inventory[new_product.prod_id] = new_product
                print(f"\nProduct added...")
            else:
                print(f"Product {self.inventory[new_product.prod_id].prod_id} "
                      f"will not be overwritten.")
        else:
            self.inventory[new_product.prod_id] = new_product
            print(f"\nProduct added...")


    def add_stock(self, prod_id, amount):
        """ Adds stock to existing product """
        if prod_id in self.inventory:
            self.inventory[prod_id].quantity += amount
            print(f"\nIncreased {self.inventory[prod_id].prod_id},"
                  f" {self.inventory[prod_id].name}'s "
                  f"stock to {self.inventory[prod_id].quantity}")
            print()
        else:
            print(f"\nNo product with ID: {prod_id} found.\n")

    def remove_stock(self, prod_id, amount):
        """ Removes stock to existing product - checks for minus figures"""
        if prod_id in self.inventory:
            if (self.inventory[prod_id].quantity - amount) < 0:
                print(f"\nERROR: Removing {amount} from {self.inventory[prod_id].prod_id}, "
                      f"{self.inventory[prod_id].name} would put you into minus figures\n")
            else:
                self.inventory[prod_id].quantity -= amount
                print(f"\nDecreased {self.inventory[prod_id].prod_id}, "
                      f"{self.inventory[prod_id].name}'s stock to"
                      f" {self.inventory[prod_id].quantity}")
                print()
        else:
            print(f"\nNo product with ID: {prod_id} found.\n")

    def update_price(self, prod_id, new_price):
        """ Updates price on existing product """
        if prod_id in self.inventory:
            self.inventory[prod_id].price = new_price
            print(f"\n{self.inventory[prod_id].prod_id}, {self.inventory[prod_id].name}'s "
                  f"price updated to: {self.inventory[prod_id].price}")
        else:
            print(f"\nNo product with ID: {prod_id} found.\n")
        print()

    def show_inventory(self):
        """ Lists all inventory by ID """
        output_string = ""
        for key, value in self.inventory.items():
            output_string += f"ID: {key}\n"
            output_string += f"  {value.name}, Price: {value.price}, Quantity: {value.quantity}\n"
        return output_string

    def find_product(self, prod):
        """ Finds a single product by ID and returns a string to display in the menu"""
        output_string = ""
        product_count = 0
        # pylint: disable=unused-variable
        for product, details in self.inventory.items():
            if details.prod_id == prod:
                product_count += 1
                output_string += f"Product: {details.prod_id}\n"
                output_string += f"Name: {details.name}\n"
                output_string += f"Price: {details.price}\n"
                output_string += f"ID: {details.prod_id}\n"
                output_string += f"Quantity: {details.quantity}\n"
        return output_string

        # pylint: disable=unreachable
        if product_count == 0:
            print(f"No product found for ID: {prod}")

    def delete_product_by_id(self, prod):
        """ Removes a product by ID """
        output_string = ""
        try:
            output_string += f"Product {self.inventory[prod].prod_id} - deleted."
            del self.inventory[prod]
        except:
            output_string += f"ID {prod} not found!"
        return output_string
