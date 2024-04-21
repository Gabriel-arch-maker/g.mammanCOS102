import tkinter as tk
from tkinter import messagebox

# Creating the GUI
root = tk.Tk()
root.title("SIMI SERVICE PAYMENT SLIP PRINTER")
root.geometry("1000x600")

# Price calculation function
from tkinter import messagebox

def price_checkout():
    location = location_entry.get().strip().lower()
    weight = int(weight_entry.get().strip().lower())
    
    if location == "epe" and weight >= 10:
        price = 10000
    elif weight < 10:
        price = 5000
    elif location == "ibeju lekki" and weight >= 10:
        price = 5000
    elif weight < 10:
        price = 3500
    else:
        messagebox.showwarning("Invalid", "Invalid location or weight combination")
        return  # Stop execution if the combination is invalid

    messagebox.showinfo("Price", f"The price is: {price}")




        

# Location entry
location_label = tk.Label(root, text="Location:")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

# Weight entry
weight_label = tk.Label(root, text="Weight:")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Button to calculate price
calculate_button = tk.Button(root, text="Calculate Price", command=price_checkout)
calculate_button.pack()

root.mainloop()
