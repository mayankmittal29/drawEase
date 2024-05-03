import tkinter as tk
line_length = 0
def draw_line(event):
    global line_length
    print('yes')
    x0, y0 = canvas.canvasx(event.x)-((float(line_length.get()))/2), canvas.canvasy(event.y)
    x1, y1 = x0 + (float(line_length.get())/2), y0 
    print(x0, y0, x1, y1)
    canvas.create_line(x0, y0, x1, y1, tags="line")
def draw_rectangle(event):
    global line_length
    x0, y0 = canvas.canvasx(event.x), canvas.canvasy(event.y)
    x1, y1 = x0 + float(line_length.get()), y0 + float(line_length.get())
    canvas.create_rectangle(x0, y0, x1, y1, tags="rectangle")
def move_line(event):
    global line_length
    x0, y0 = canvas.canvasx(event.x), canvas.canvasy(event.y)
    x1, y1 = x0 + line_length.get(), y0 + line_length.get()
    canvas.coords("line", x0, y0, x1, y1)
def function1(root):
    global line_length
    line_length = tk.Entry(root)
    line_length.pack()
# Create the main window
root = tk.Tk()
root.title("Drawing Editor")

# Create a canvas widget
canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Add a label and entry for line length
# line_length_label = tk.Label(root, text="Line Length:")
clear_button = tk.Button(root, text="draw line", command=function1(root))
clear_button.pack()

# line_length_label.pack()
# line_length = tk.Entry(root)
# line_length.pack()
# line_length = tk.Entry(root)
# line_length.pack()

# Bind the canvas to respond to mouse events
canvas.bind("<Button-1>", draw_rectangle)
canvas.bind("<B1-Motion>", move_line)

# Start the Tkinter event loop
root.mainloop()
