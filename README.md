# product_inventory
## Product Inventory Manager - Tkinter GUI - Made with Python 3.8

# Descripton
This program uses a combination classes, Tkinter and pickle to simulate a product inventory.

The manager contains 4 classes of the following:
- main.py       - runs the main script
- menu.py       - initializes the tkinter menu
- inventory.py  - manages the inventory
- product.py    - instantiates a single product

The inventory has the following GUI:

![Inventory](https://github.com/benico50/product_inventory/blob/master/Inventory.PNG)

# To start the program
- Run main.py
- Program has some validation to check for an existing text file called data.txt in root. If the text file contains no information, the program will still run. **The program will fail if data.txt does not exist.**

# Validation
Basic validation has been implemented. Errors will only be produced in the console at the time of writing (24/04/2020). Issues like not being able to find a product ID.

# Refactoring
Some basic refactoring has been completed. As this is one of my first projects, I'm attempting to balance refactors with code readability. This will improve over time.

# PEP
Pylint has been used as a baseline.

# Contribution
Access to contribute has been restricted currently. This is due to me wanting to remove an element of confusion in my own code base. I plan to open this up once I'm more comfortable.

# Planned improvements
- Increase the readability of the inventory display. Currently product ID's and their information aren't showing in an optimal format.
- Tweak GUI to better display labels and contents
- Force GUI window on additional Tkinter windows
- Allow additional product information to be added
- Allow other inventory search terms - rather than just by ID

