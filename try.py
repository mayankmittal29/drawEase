import tkinter as tk

def add_input():
    new_entry = tk.Entry(root)
    new_entry.pack()

# Create the main window
root = tk.Tk()
root.title("Add Inputs")

# Create a button to add inputs
add_button = tk.Button(root, text="Add Input", command=add_input)
add_button.pack()

# Start the Tkinter event loop
root.mainloop()
