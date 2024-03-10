"""
Author:  Nickolaus Macy
Date written: 3/2/24
Assignment: Final Project
Short Desc:  Pizza Ordering System
"""


# Import tkinter module
import tkinter as tk
from tkinter import messagebox


# Define the main window
root = tk.Tk()
root.title("Tony's Pizzeria")
root.geometry("800x600")


# Define a function to open the order window
def open_order_window():
    # Create a new window
    order_window = tk.Toplevel(root)
    order_window.title("Order Pizza")
    order_window.geometry("800x600")



    # Create a label to display the order instructions
    order_label = tk.Label(order_window, text="Please enter your name, phone number, and pizza size (S, M, L, or XL) in the entry boxes below.", font=("Arial", 16), bg="white")
    order_label.pack(pady=20)

    # Create a frame to hold the entry boxes and labels
    entry_frame = tk.Frame(order_window, bg="white")
    entry_frame.pack()

    # Create a label and an entry box for the name
    name_label = tk.Label(entry_frame, text="Name:", font=("Arial", 14), bg="white")
    name_label.grid(row=0, column=0, padx=10, pady=10)
    name_entry = tk.Entry(entry_frame, font=("Arial", 14), bg="white")
    name_entry.grid(row=0, column=1, padx=10, pady=10)

    # Create a label and an entry box for the phone number
    phone_label = tk.Label(entry_frame, text="Phone:", font=("Arial", 14), bg="white")
    phone_label.grid(row=1, column=0, padx=10, pady=10)
    phone_entry = tk.Entry(entry_frame, font=("Arial", 14), bg="white")
    phone_entry.grid(row=1, column=1, padx=10, pady=10)

    # Create a label and an entry box for the pizza size
    size_label = tk.Label(entry_frame, text="Size:", font=("Arial", 14), bg="white")
    size_label.grid(row=2, column=0, padx=10, pady=10)
    size_entry = tk.Entry(entry_frame, font=("Arial", 14), bg="white")
    size_entry.grid(row=2, column=1, padx=10, pady=10)

    # Define a function to validate the user input and place the order
    def validate_and_order():
        # Get the user input from the entry boxes
        name = name_entry.get()
        phone = phone_entry.get()
        size = size_entry.get()

        # Check if the user input is valid
        if name == "" or phone == "" or size == "":
            # If any entry box is empty, show an error message
            error_message = tk.messagebox.showerror(title="Error", message="Please fill in all the entry boxes.")
        elif not phone.isdigit():
            # If the phone number is not a number, show an error message
            error_message = tk.messagebox.showerror(title="Error", message="Please enter a valid phone number.")
        elif size.upper() not in ["S", "M", "L", "XL"]:
            # If the pizza size is not one of the options, show an error message
            error_message = tk.messagebox.showerror(title="Error", message="Please enter a valid pizza size (S, M, L, or XL).")
        else:
            # If the user input is valid, show a confirmation message and close the order window
            confirmation_message = tk.messagebox.showinfo(title="Confirmation", message=f"Thank you, {name}! Your order for a {size.upper()} pizza has been placed. We will call you at {phone} when your pizza is ready.")
            order_window.destroy()

    # Create a button to validate the user input and place the order
    order_button = tk.Button(order_window, text="Order", font=("Arial", 14), bg="white", command=validate_and_order)
    order_button.pack(pady=20)

    # Create a button to close the order window
    close_button = tk.Button(order_window, text="Close", font=("Arial", 14), bg="white", command=order_window.destroy)
    close_button.pack(pady=20)

# Create a label to display the welcome message
welcome_label = tk.Label(root, text="Welcome to Tony's Pizzeria!", font=("Arial", 24), bg="white")
welcome_label.pack(pady=20)

# Create a button to open the order window
order_button = tk.Button(root, text="Order Pizza", font=("Arial", 18), bg="white", command=open_order_window)
order_button.pack(pady=20)

# Create a button to exit the application
exit_button = tk.Button(root, text="Exit", font=("Arial", 18), bg="white", command=root.destroy)
exit_button.pack(pady=20)

# Start the main loop
root.mainloop()
