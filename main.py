import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
import xml.etree.ElementTree as ET
from PIL import Image, ImageTk

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800
list_of_rectangles = []
list_of_lines = []
list_of_groups = []
list_of_selected = []
def destroy_button_by_text(root, button_text):
    for widget in root.winfo_children():
        if isinstance(widget, tk.Button) and widget.cget("text") == button_text:
            widget.destroy()
            break
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
    def show_on_select(self):
        pass
    def show_properly(self):
        pass
    def delete(self):
        pass

class Line(DrawingObject):
    def __init__(self, x1, y1, x2, y2, color,id):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.dash_offset = 0

        self.id = id
    def draw(self, canvas):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill=self.color)
    def set_id(self, id):
        self.id = id
    def is_clicked(self, x, y):
        pass
    def move(self, dx, dy):
        editor.canvas.coords(self.id, self.x1 + dx, self.y1 + dy, self.x2 + dx, self.y2 + dy)
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy
    def edit(self, dialog):
        # Show dialog to edit line properties
        
        pass
    def show_on_select(self):
        editor.canvas.itemconfig(self.id, dash=(10, 10))
        self.move_dash()
        pass
    def show_properly(self):
        editor.canvas.itemconfig(self.id, dash=())
        # editor.canvas.itemconfig(self.id, dash=(5, 5))
        pass
    def ungroup(self):
        global list_of_lines
        list_of_lines.append(Line(self.x1, self.y1, self.x2, self.y2, self.color, id=self.id))
        pass
    def delete(self):
        # return super().delete()
        editor.canvas.delete(self.id)
        pass
    def move_dash(self):
        self.dash_offset += 2
        editor.canvas.itemconfig(self.id, dashoffset=self.dash_offset)
        if self.dash_offset >= 10:
            self.dash_offset = 0
        editor.canvas.after(50, self.move_dash)



class Rectangle(DrawingObject):
    def __init__(self, x1, y1, x2, y2, color, corner_style,id):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.corner_style = corner_style
        self.id = id
        self.dash_offset = 0
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.color)
    def set_id(self, id):
        self.id = id
    def is_clicked(self, x, y):
        # Check if (x, y) is inside the rectangle
        pass
    def move(self, dx, dy):
        editor.canvas.coords(self.id, self.x1 + dx, self.y1 + dy, self.x2 + dx, self.y2 + dy)
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy
    def edit(self, dialog):
        # Show dialog to edit rectangle properties
        pass
    def show_on_select(self):
        editor.canvas.itemconfig(self.id, dash=(10, 10))
        self.move_dash()
        pass
    def show_properly(self):
        editor.canvas.itemconfig(self.id, dash=())
        pass
    def ungroup(self):
        global list_of_rectangles
        list_of_rectangles.append(Rectangle(self.x1, self.y1, self.x2, self.y2, self.color, self.corner_style, id=self.id))

        pass
    def delete(self):
        # return super().delete()
        editor.canvas.delete(self.id)
        pass
    def move_dash(self):
        self.dash_offset += 2
        editor.canvas.itemconfig(self.id, dashoffset=self.dash_offset)
        if self.dash_offset >= 10:
            self.dash_offset = 0
        editor.canvas.after(50, self.move_dash)

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
        for obj in self.objects:
            obj.move(dx, dy)
        pass
    def show_on_select(self):
        for obj in self.objects:
            obj.show_on_select()
        pass
    def show_properly(self):
        for obj in self.objects:
            obj.show_properly()
        pass
    def ungroup(self):
        for obj in self.objects:
            if isinstance(obj,Group):
                list_of_groups.append(obj)
            else:
                obj.ungroup()
    def ungroupall(self):
        for obj in self.objects:
            if isinstance(obj,Group):
                for obj2 in obj.objects:
                    self.objects.append(obj2)                
                # obj.ungroupall()
                if obj in list_of_groups:
                    list_of_groups.__delitem__(list_of_groups.index(obj))
                # list_of_groups.append(obj)
            else:
                obj.ungroup()
            # obj.ungroupall()
        # Remove the group and add its objects to the canvas
        pass
    def delete(self):
        # return super().delete()
        for obj in self.objects:
            obj.delete()
        pass
current_rectangle = None
current_line = None
choice = 'draw'
start_x, start_y = 0, 0 
def generate_group_code():
    global list_of_groups
    ascii_code = 'begin\n'
    for group in list_of_groups:
            for obj in group.objects:
                if isinstance(obj,Line):
                    ascii_code += 'line '+ str(obj.x1)+' '+ str(obj.y1)+' '+ str(obj.x2)+' '+ str(obj.y2)+' '+ obj.color+'\n'
                if isinstance(obj,Rectangle):
                    ascii_code += 'rectangle '+ str(obj.x1)+' '+ str(obj.y1)+' '+ str(obj.x2)+' '+ str(obj.y2)+' '+ obj.color+' '+ obj.corner_style+'\n'
                else:
                    ascii_code+=generate_group_code()
    ascii_code+= 'end\n'
    return ascii_code
    
class DrawingEditor:
    global canvas
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        self.objects = []
        self.selected_object = False
        self.code = ''
        self.asciicode = ''
        
        # Add toolbar buttons and menu items for drawing operations
        self.create_menu()
        self.create_toolbar()
        # Bind mouse events
        # self.canvas.bind("<Button-1>", self.on_click)

            # Bind the canvas to respond to mouse events
        image33 = Image.open("s2.png")
        image33 = image33.resize((30, 30))
        self.imag1 = ImageTk.PhotoImage(image33)
        self.canvas.button = tk.Button(root, text="draw rectangle",image=self.imag1, command=self.create_rectangle)
        self.canvas.button.pack(side=tk.LEFT, padx=10, pady=10)
        image333 = Image.open("s3.png")
        image333 = image333.resize((30, 30))
        self.imag2 = ImageTk.PhotoImage(image333)
        self.canvas.button = tk.Button(root, text="draw line", image=self.imag2, command=self.create_line)
        self.canvas.button.pack(side=tk.LEFT, padx=10, pady=10)
        image = Image.open("s1.png")
        image = image.resize((30, 30))
        self.image = ImageTk.PhotoImage(image)
        self.canvas.button = tk.Button(root, text="select", image=self.image, command=self.select_object)
        self.canvas.button.pack(side=tk.LEFT, padx=10, pady=10)
        # self.canvas.bind("<Button-1>", self.on_click)

    
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
    def generate_code(self):
        self.asciicode = ''
        for line in list_of_lines:
            # self.objects.append(line)
            self.asciicode += 'line '+str(line.x1)+' '+ str(line.y1)+' '+ str(line.x2)+' '+ str(line.y2)+' '+ line.color+'\n'
        for rectangle in list_of_rectangles:
            # self.objects.append(rectangle)
            self.asciicode += 'rectangle '+str(rectangle.x1)+' '+ str(rectangle.y1)+' '+ str(rectangle.x2)+' '+ str(rectangle.y2)+' '+ rectangle.color+' '+rectangle.corner_style+'\n'
        # for group in list_of_groups:
        self.asciicode+=generate_group_code()
        print(self.asciicode)
    def save_drawing(self, filename):
        self.generate_code()
        with open(filename, 'w') as file:
            file.write(self.asciicode)
    
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
        global list_of_selected

        # Deselect the currently selected object
        if self.selected_object:
            for obj in list_of_selected:
                obj.show_properly()
            self.selected_object = False
            choice = 'draw'
            destroy_button_by_text(self.root, "group")
            destroy_button_by_text(self.root, "move")
            destroy_button_by_text(self.root, "ungroup")
            destroy_button_by_text(self.root, "ungroup-all")
            destroy_button_by_text(self.root, "delete")
            list_of_selected.clear()
            return 
        
        # Select the new object
        self.selected_object = True
        self.create_rectangle()
        choice = 'select'
        self.canvas.button = tk.Button(root, text="group", command=self.remove_rectangle)
        self.canvas.button.pack(side=tk.LEFT, padx=10, pady=10)
        self.canvas.button = tk.Button(root, text="move", command=self.move_object)
        self.canvas.button.pack(side=tk.LEFT, padx=10, pady=10)
        self.canvas.button = tk.Button(root, text="ungroup", command=self.ungroup)
        self.canvas.button.pack(side=tk.LEFT, padx=10, pady=10)
        self.canvas.button = tk.Button(root, text="ungroup-all", command=self.ungroupall)
        self.canvas.button.pack(side=tk.LEFT, padx=10, pady=10)
        self.canvas.button = tk.Button(root, text="delete", command=self.delete)
        self.canvas.button.pack(side=tk.LEFT, padx=10, pady=10)
    def ungroup(self):
        for obj in list_of_selected:
            if isinstance(obj,Group):
                # list_of_groups.append(obj)
                obj.ungroup()
                list_of_groups.__delitem__(list_of_groups.index(obj))
    def delete(self):
        for obj in list_of_selected:
            obj.delete()
            if isinstance(obj,Line):
                list_of_lines.__delitem__(list_of_lines.index(obj))
            if isinstance(obj,Rectangle):
                list_of_rectangles.__delitem__(list_of_rectangles.index(obj))
            if isinstance(obj,Group):
                list_of_groups.__delitem__(list_of_groups.index(obj))
        list_of_selected.clear()
    def ungroupall(self):
        # global list_of_groups
        for group in list_of_selected:
            if isinstance(group,Group):
                group.ungroupall()
                list_of_groups.__delitem__(list_of_groups.index(group))
    def move_object(self):
        self.canvas.bind("<Button-1>",  self.start_move)
        self.canvas.bind("<B1-Motion>", self.move_object1)
        self.canvas.bind("<ButtonRelease-1>", self.end_move1)
        
    def start_move(self, event):
        global start_x, start_y
        start_x, start_y = event.x, event.y
    def move_object1(self, event):
        global start_x, start_y
        global list_of_selected
        
        x, y = event.x, event.y
        dx, dy = x - start_x, y - start_y
        for obj in list_of_selected:
            print('on time of moving check ', obj)
            obj.move(dx, dy)
        for obj in list_of_groups:
            print('object', obj)
            # obj.move(dx, dy)
        start_x, start_y = x, y
    def end_move1(self, event):
        global choice
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        choice = 'draw'
        pass
    def remove_rectangle(self):
        # self.canvas.bind("<Button-1>", remove_rectangle)
        new_group = Group()
        global list_of_selected
        for obj in list_of_selected:
            if isinstance(obj, Line):
                list_of_lines.__delitem__(list_of_lines.index(obj))
            if isinstance(obj, Rectangle):
                list_of_rectangles.__delitem__(list_of_rectangles.index(obj))
            new_group.add_object(obj)
            
        list_of_groups.append(new_group)
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
    global start_x, start_y, current_rectangle, choice, list_of_selected
    
    if current_rectangle:
        x, y = event.x, event.y
        editor.canvas.coords(current_rectangle, start_x, start_y, x, y)
        if choice == 'select':
           
            for line in list_of_lines:
                if line.x1 >= start_x and line.y1 >= start_y and line.x2 <= x and line.y2 <= y:
                    list_of_selected.append(line)
            for rectangle in list_of_rectangles:
                if rectangle.x1 >= start_x and rectangle.y1 >= start_y and rectangle.x2 <= x and rectangle.y2 <= y:
                    list_of_selected.append(rectangle)
            for group in list_of_groups:
                for obj in group.objects:
                    if isinstance(obj,Line) and obj.x1 >= start_x and obj.y1 >= start_y and obj.x2 <= x and obj.y2 <= y:
                        list_of_selected.append(group)
                        break
                    elif isinstance(obj,Rectangle) and obj.x1 >= start_x and obj.y1 >= start_y and obj.x2 <= x and obj.y2 <= y:
                        list_of_selected.append(group)
                        break
            for obj in list_of_selected:
                obj.show_on_select()
            editor.canvas.delete(current_rectangle)
            
            return
        list_of_rectangles.append(Rectangle(start_x, start_y, x, y, "black", "sharp", id=current_rectangle))
def start_line(event):
    global start_x, start_y, current_line
    start_x, start_y = event.x, event.y
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
        list_of_lines.append(Line(start_x, start_y, x, y, "black", id=current_line))
# Example usage
root = tk.Tk()
root.title("Drawing Editor")
editor = DrawingEditor(root)
root.mainloop()

print('gopal')
print(list_of_lines)
print('list of rectangles')
print(list_of_rectangles)
print('list of groups')
for group in list_of_groups:
    print('new_group')
    print(group)
    for obj in group.objects:
        print(obj, end='')  # print all objects in the group