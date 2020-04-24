""" Menu Class to implement Tkinter GUI"""
import pickle
from tkinter import Tk, Label, Entry, Button, Text, END, Scrollbar, NONE
from inventory import Inventory


class Menu:
    """ Menu Class"""
    # pylint: disable=too-many-instance-attributes
    def __init__(self):
        self.inv = Inventory()
        try:
            self.infile = open("data.txt", "rb")
            self.save_file = pickle.load(self.infile)
            self.inv.inventory = self.save_file
            self.infile.close()
        except EOFError:
            print("File is empty - starting with an empty database.")

        self.master = Tk()
        self.master.geometry("700x300")
        self.master.resizable(width=False, height=False)
        self.master.title("Product Inventory")
        inv_1 = Label(self.master, text="1. Show Inventory", font=("Helvetica", 14))
        inv_1.grid(row=0, column=0, sticky="w")
        inv_2 = Label(self.master, text="2. Create a new product", font=("Helvetica", 14))
        inv_2.grid(row=1, column=0, sticky="w")
        inv_3 = Label(self.master, text="3. Increase stock", font=("Helvetica", 14))
        inv_3.grid(row=2, column=0, sticky="w")
        inv_4 = Label(self.master, text="4. Decrease stock", font=("Helvetica", 14))
        inv_4.grid(row=3, column=0, sticky="w")
        inv_5 = Label(self.master, text="5. Update price", font=("Helvetica", 14))
        inv_5.grid(row=4, column=0, sticky="w")
        inv_6 = Label(self.master, text="6. Find product details", font=("Helvetica", 14))
        inv_6.grid(row=5, column=0, sticky="w")
        inv_7 = Label(self.master, text="7. Delete a product", font=("Helvetica", 14))
        inv_7.grid(row=6, column=0, sticky="w")

        self.btn_show_inventory = Button(self.master, text="*", command=self.show_inv)
        self.btn_show_inventory.grid(row=0, column=1)

        self.btn_create_product = Button(self.master, text="*", command=self.create_product)
        self.btn_create_product.grid(row=1, column=1)

        self.btn_increase_stock = Button(self.master, text="*", command=self.increase_stock)
        self.btn_increase_stock.grid(row=2, column=1)

        self.btn_decrease_stock = Button(self.master, text="*", command=self.decrease_stock)
        self.btn_decrease_stock.grid(row=3, column=1)

        self.btn_update_price = Button(self.master, text="*", command=self.update_price)
        self.btn_update_price.grid(row=4, column=1)

        self.btn_find_product = Button(self.master, text="*", command=self.find_product)
        self.btn_find_product.grid(row=5, column=1)

        self.btn_delete_product = Button(self.master, text="*", command=self.delete_product)
        self.btn_delete_product.grid(row=6, column=1)

        self.btn_quit = Button(self.master, text="Quit", command=self.quit, font=("Helvetica", 14))
        self.btn_quit.grid(row=7, column=0)

        self.scroll = Scrollbar(self.master)
        self.scroll.place(x=660, y=0)
        self.inventory_box = Text(self.master, height=12, width=50, wrap=NONE,
                                  yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.inventory_box.yview)
        self.inventory_box.place(x=250, y=0)

        self.master.mainloop()

    def create_product(self):
        """ Creates a new product in the inventory"""
        def get_product_details():
            product_details = name_box.get(), price_box.get(), id_box.get(), quantity_box.get()
            self.inv.create_product(product_details)
            with open("data.txt", "wb") as outfile:
                pickle.dump(self.inv.inventory, outfile)
            new_win.destroy()
            self.show_inv()

        new_win = Tk()
        new_win.geometry("270x150")
        new_win.title("Create new product")
        lbl_id = Label(new_win, text="Product ID:", font=("Helvetica", 12))
        lbl_id.grid(row=0, column=0, sticky="w")
        lbl_name = Label(new_win, text="Product Name:", font=("Helvetica", 12))
        lbl_name.grid(row=1, column=0, sticky="w")
        lbl_price = Label(new_win, text="Product Price:", font=("Helvetica", 12))
        lbl_price.grid(row=2, column=0, sticky="w")
        lbl_quantity = Label(new_win, text="Product Quantity:", font=("Helvetica", 12))
        lbl_quantity.grid(row=3, column=0, sticky="w")

        id_box = Entry(new_win)
        id_box.grid(row=0, column=1)

        name_box = Entry(new_win)
        name_box.grid(row=1, column=1)

        price_box = Entry(new_win)
        price_box.grid(row=2, column=1)

        quantity_box = Entry(new_win)
        quantity_box.grid(row=3, column=1)

        btn_get_product_details = Button(new_win, text="Submit", command=get_product_details)
        btn_get_product_details.place(x=100, y=110)

    def increase_stock(self):
        """ Increases product stock by ID"""
        def get_stock_increase():
            self.inv.add_stock(id_box.get(), int(stock_box.get()))

            with open("data.txt", "wb") as outfile:
                pickle.dump(self.inv.inventory, outfile)
            new_win.destroy()
            self.show_inv()

        new_win = Tk()
        new_win.geometry("270x150")
        new_win.title("Increase stock")
        lbl_id = Label(new_win, text="Product ID:", font=("Helvectica", 12))
        lbl_id.grid(row=0, column=0, sticky="w")
        lbl_stock = Label(new_win, text="Increase stock by:", font=("Helvectica", 12))
        lbl_stock.grid(row=1, column=0, sticky="w")

        id_box = Entry(new_win)
        id_box.grid(row=0, column=1)

        stock_box = Entry(new_win)
        stock_box.grid(row=1, column=1)

        btn_get_stock_inrease_details = Button(new_win, text="Submit", command=get_stock_increase)
        btn_get_stock_inrease_details.place(x=100, y=110)

    def decrease_stock(self):
        """ Decreases product stock by ID """
        def get_stock_decrease():
            self.inv.remove_stock(id_box.get(), int(stock_box.get()))

            with open("data.txt", "wb") as outfile:
                pickle.dump(self.inv.inventory, outfile)

            new_win.destroy()
            self.show_inv()

        new_win = Tk()
        new_win.geometry("270x150")
        new_win.title("Increase stock")
        lbl_id = Label(new_win, text="Product ID:", font=("Helvectica", 12))
        lbl_id.grid(row=0, column=0, sticky="w")
        lbl_stock = Label(new_win, text="Decrease stock by:", font=("Helvectica", 12))
        lbl_stock.grid(row=1, column=0, sticky="w")

        id_box = Entry(new_win)
        id_box.grid(row=0, column=1)

        stock_box = Entry(new_win)
        stock_box.grid(row=1, column=1)

        btn_get_stock_decrease_details = Button(new_win, text="Submit", command=get_stock_decrease)
        btn_get_stock_decrease_details.place(x=100, y=110)

    def update_price(self):
        """ Updates product price by ID """
        def get_price_increase():
            self.inv.update_price(id_box.get(), int(price_box.get()))

            with open("data.txt", "wb") as outfile:
                pickle.dump(self.inv.inventory, outfile)

            new_win.destroy()
            self.show_inv()

        new_win = Tk()
        new_win.geometry("270x150")
        new_win.title("Update price")
        Label(new_win, text="Product ID:", font=("Helvetica", 12)).grid(row=0, column=0, sticky="w")
        Label(new_win, text="New Price:", font=("Helvetica", 12)).grid(row=1, column=0, sticky="w")

        id_box = Entry(new_win)
        id_box.grid(row=0, column=1)

        price_box = Entry(new_win)
        price_box.grid(row=1, column=1)

        btn_get_price_increase_details = Button(new_win, text="Submit", command=get_price_increase)
        btn_get_price_increase_details.place(x=100, y=110)

    def find_product(self):
        """ Finds and displays single product information by ID """
        def get_product_details():
            output_string = self.inv.find_product(id_box.get())
            print(output_string)

            product_box.delete("1.0", "end")
            product_box.insert(END, output_string)

        new_win = Tk()
        new_win.geometry("450x170")
        new_win.title("Find product")

        id_label = Label(new_win, text="Product ID:", font=("Helvetica", 12))
        id_label.place(x=70, y=10)

        id_box = Entry(new_win)
        id_box.place(x=160, y=12)

        product_box = Text(new_win, height=5, width=30, wrap=NONE)
        product_box.place(x=100, y=70)

        btn_get_product_details = Button(new_win, text="Submit", command=get_product_details)
        btn_get_product_details.place(x=320, y=8)

    def delete_product(self):
        """ Deletes a product by ID """
        def delete_a_product():
            lbl_deleted = Label(new_win, text=self.inv.delete_product_by_id(id_box.get()),
                                font=("Helvetica", 12))
            lbl_deleted.place(x=80, y=90)

            with open("data.txt", "wb") as outfile:
                pickle.dump(self.inv.inventory, outfile)

            self.show_inv()

        new_win = Tk()
        new_win.geometry("300x150")
        new_win.title("Delete product")

        id_label = Label(new_win, text="Product ID:", font=("Helvetica", 12))
        id_label.place(x=30, y=10)

        id_box = Entry(new_win)
        id_box.place(x=130, y=12)

        btn_delete_product = Button(new_win, text="Submit", command=delete_a_product)
        btn_delete_product.place(x=120, y=50)

    def quit(self):
        """ Quits the Main Menu"""
        self.master.destroy()

    def show_inv(self):
        """ Displays the full inventory """
        content = self.inv.show_inventory()
        self.inventory_box.delete("1.0", "end")
        self.inventory_box.insert(END, content)
