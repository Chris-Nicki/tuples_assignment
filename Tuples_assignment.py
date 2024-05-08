# Tuples

# 1. Tuple Mastery in Python
"""Objective:
The aim of this assignment is to deepen your understanding of tuples in Python, along with their 
interaction with lists, dictionaries, and basic Python functionalities like functions, input handling, 
and string formatting. By completing this assignment, you will enhance your skills in data structuring, 
manipulation, and application of tuples in practical scenarios.
"""
# Task 1: Formatting Flight Itineraries
"""Create a Python function that takes a list of tuples as an argument. Each tuple contains information 
about a flight itinerary: (traveler_name, origin, destination). The function should format and return a 
string that lists each itinerary. For example, if the input is [("Alice", "New York", "London"), 
("Bob", "Tokyo", "San Francisco")], the output should be a string formatted as:
"""

    # "Itinerary 1: Alice - From New York to London
    # Itinerary 2: Bob - From Tokyo to San Francisco"

itineraries = [("Chris", "Denver", "Chicago"), ("Hank", "Denver","Hawaii")]

def airport_printer():
    for name, origin, destination in itineraries:
        print(f"{name} - From {origin} to {destination}")
airport_printer()


# 2. Python Data Structure Challenges in Real-World Scenarios
"""Objective:
This assignment is designed to enhance your understanding and application of Python's core data 
structures - tuples, lists, and dictionaries - in real-world contexts. By engaging with these tasks, 
you will practice manipulating these data structures, applying built-in Python methods, and implementing 
error handling in practical situations.
"""
# Task 1:  Library System Enhancement
"""Problem Statement:
You are maintaining a library system where each book is stored as a tuple within a list. Your task is to 
update this system by adding new books and ensuring no duplicates.
"""
# Existing Library Data:
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
# Add functionality to insert new books into library.
# Ensure that adding a duplicate book is handled appropriately.

def add_books(books):
    for title, author in library:
        if books[0] == title:
            print("Sorry, title already in inventory. Please enter a different book")
            return library
    library.append(books)
    return library
print(add_books(("The Hitchhiker's Guide to the Galaxy" , "Douglas Adams")))
print(add_books(("It", "Stephen King")))
print(add_books(("Rainbow 6", "Tom Clancy")))
print(add_books(("The Art of Barbecue", "Chris Nicki")))
print(add_books(("1984", "George Orwell")))
print(add_books(("It", "Stephen King")))

# # 3. Mastering Tuple Packing and Unpacking in Python
# """
# Objective: 
# The goal of this assignment is to deepen your understanding of tuple packing and unpacking in Python. 
# You will apply these techniques in various practical scenarios, enhancing your ability to work with 
# flexible data structures and improve data handling efficiency
# """
# # Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.
# """Problem Statement: You are given a list of tuples, each representing a customer's order. Each tuple 
# contains the customer's name, the product ordered, and the quantity. Your task is to unpack each tuple 
# and print the order details in a user-friendly format.
# """
# Sample Order Data:
orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("KT", "Phone", 10),
    ("Matt", "VR Headset", 2)
]
for name, item, quantity in orders:
    print(f"{name} got {quantity} {item}")

