import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
list_of_rectangles = []
list_of_lines = []
list_of_groups = []
class DrawingObject:
    def __init__(self):
        self.selected = False
    def is_clicked(self, x, y):
        pass
    def delete(self):
        pass
    def copy(self):
        pass
    def move(self, dx, dy):
        pass

class Line(DrawingObject):
    def __init__(self, x1, y1, x2, y2, color):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
    
    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color)
    
    def is_clicked(self, x, y):
        pass
    
    def edit(self, dialog):
        # Show dialog to edit line properties
        pass

class Rectangle(DrawingObject):
    def __init__(self, x1, y1, x2, y2, color, corner_style):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.corner_style = corner_style
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.color)
    
    def is_clicked(self, x, y):
        # Check if (x, y) is inside the rectangle
        pass
    
    def edit(self, dialog):
        # Show dialog to edit rectangle properties
        pass

class Group(DrawingObject):
    def __init__(self):
        super().__init__()
        self.objects = []
    
    def add_object(self, obj):
        self.objects.append(obj)
    
    def draw(self, canvas):
        for obj in self.objects:
            obj.draw(canvas)
    
    def is_clicked(self, x, y):
        # Check if (x, y) is inside any object in the group
        pass
    
    def delete(self):
        # Delete all objects in the group
        pass
    
    def copy(self):
        # Copy all objects in the group
        pass
    
    def move(self, dx, dy):
        # Move all objects in the group by (dx, dy)
        pass

current_rectangle = None
current_line = None
choice = 'draw'

class DrawingEditor:
    global canvas
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        self.objects = []
        self.selected_object = None
        
        # Add toolbar buttons and menu items for drawing operations
        self.create_menu()
        self.create_toolbar()
        # Bind mouse events
        # self.canvas.bind("<Button-1>", self.on_click)

# Bind the canvas to respond to mouse events
        self.canvas.button = tk.Button(root, text="draw rectangle", command=self.create_rectangle)
        self.canvas.button.pack()
        self.canvas.button = tk.Button(root, text="draw line", command=self.create_line)
        self.canvas.button.pack()
        self.canvas.button = tk.Button(root, text="select", command=self.select_object)
        self.canvas.button.pack()
        

    
    def create_menu(self):
        # Create menu for file operations
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)
        
        file_menu = tk.Menu(self.menu, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        self.menu.add_cascade(label="File", menu=file_menu)
    
    def create_toolbar(self):
        # Create toolbar with drawing tools
        pass
    def create_line(self):
        self.canvas.bind("<Button-1>", start_line)
        self.canvas.bind("<B1-Motion>", draw_line)
        self.canvas.bind("<ButtonRelease-1>", end_line)
    def create_rectangle(self):
        self.canvas.bind("<Button-1>", start_rectangle)
        self.canvas.bind("<B1-Motion>", draw_rectangle)
        self.canvas.bind("<ButtonRelease-1>", end_rectangle)
    def open_file(self):
        filename = filedialog.askopenfilename(filetypes=[("Drawing Files", "*.txt")])
        if filename:
            self.load_drawing(filename)
    
    def save_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Drawing Files", "*.txt")])
        if filename:
            self.save_drawing(filename)
    
    def load_drawing(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                # Parse each line and create corresponding drawing objects
                pass
    
    def save_drawing(self, filename):
        with open(filename, 'w') as file:
            for obj in self.objects:
                file.write(obj.to_file_format() + "\n")
    
    def on_click(self, event):
        # Handle mouse click events
        x, y = event.x, event.y
        
        # Check if an object is clicked
        for obj in reversed(self.objects):
            if obj.is_clicked(x, y):
                self.select_object(obj)
                break
    
    def select_object(self):
        global choice

        # Deselect the currently selected object
        if self.selected_object:
            self.selected_object = False
            choice = 'draw'
        
        # Select the new object
        self.selected_object = True
        self.create_rectangle()
        choice = 'select'
        self.canvas.button = tk.Button(root, text="group", command=self.remove_rectangle)
        self.canvas.button.pack()
    def remove_rectangle(self):
        self.canvas.bind("<Button-1>", remove_rectangle)

    def redraw_canvas(self):
        self.canvas.delete("all")
        for obj in self.objects:
            obj.draw(self.canvas)
def start_rectangle(event):
    global start_x, start_y, current_rectangle
    start_x, start_y = event.x, event.y
    if choice == 'select':
        current_rectangle = editor.canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="grey", dash=(5, 5))
    else:
        current_rectangle = editor.canvas.create_rectangle(start_x, start_y, start_x, start_y, outline="grey")

        
def draw_rectangle(event):
    if current_rectangle:
        x, y = event.x, event.y
        editor.canvas.coords(current_rectangle, start_x, start_y, x, y)
    # print(start_x, start_y, x, y)
def end_rectangle(event):
    global start_x, start_y, current_rectangle
    if current_rectangle:
        x, y = event.x, event.y
        editor.canvas.coords(current_rectangle, start_x, start_y, x, y)
        # print(f"Rectangle coordinates: ({start_x}, {start_y}) - ({x}, {y})")
        if choice == 'select':
            # editor.canvas.delete(current_line)
            grp_obje = Group()
            # grp_obje.add_object(list_of_lines[-1])
            for line in list_of_lines:
                # grp_obje.add_object(line)
                if line.x1 >= start_x and line.y1 >= start_y and line.x2 <= x and line.y2 <= y:
                    grp_obje.add_object(line)
                    list_of_lines.__delitem__(list_of_lines.index(line))
            for rectangle in list_of_rectangles:
                if rectangle.x1 >= start_x and rectangle.y1 >= start_y and rectangle.x2 <= x and rectangle.y2 <= y:
                    grp_obje.add_object(rectangle)
                    list_of_rectangles.__delitem__(list_of_rectangles.index(rectangle))
            for group in list_of_groups:
                if group.objects[0].x1 >= start_x and group.objects[0].y1 >= start_y and group.objects[0].x2 <= x and group.objects[0].y2 <= y:
                    grp_obje.add_object(group)
                    list_of_groups.__delitem__(list_of_groups.index(group))
            list_of_groups.append(grp_obje)
            return
        list_of_rectangles.append(Rectangle(start_x, start_y, x, y, "black", "sharp"))
def remove_rectangle(event):
    global current_rectangle
    if current_rectangle and choice == 'select':
        canvas.delete(current_rectangle)
        current_rectangle = None
def start_line(event):
    global start_x, start_y, current_line
    start_x, start_y = event.x, event.y
    print(start_x, start_y)
    current_line = editor.canvas.create_line(start_x, start_y, start_x, start_y, tags="line")

def draw_line(event):
    if current_line:
        x, y = event.x, event.y
        editor.canvas.coords(current_line, start_x, start_y, x, y)
def end_line(event):
    global start_x, start_y, current_line
    if current_line:
        x, y = event.x, event.y
        editor.canvas.coords(current_line, start_x, start_y, x, y)
        # print(f"Line coordinates: ({start_x}, {start_y}) - ({x}, {y})")
        list_of_lines.append(Line(start_x, start_y, x, y, "black"))
# Example usage
root = tk.Tk()
root.title("Drawing Editor")
editor = DrawingEditor(root)
root.mainloop()
print(list_of_rectangles)
print(list_of_lines)
# print(list_of_groups)
for group in list_of_groups:
    print(group.objects)