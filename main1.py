import tkinter as tk
from tkinter import filedialog
import xml.etree.ElementTree as ET
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
        
        
def draw_rounded_rectangle(canvas, x1, y1, x2, y2, corner_radius, **kwargs):
    # Draw the four sides of the rectangle
    canvas.create_line(x1 + corner_radius, y1, x2 - corner_radius, y1, **kwargs)
    canvas.create_line(x2, y1 + corner_radius, x2, y2 - corner_radius, **kwargs)
    canvas.create_line(x2 - corner_radius, y2, x1 + corner_radius, y2, **kwargs)
    canvas.create_line(x1, y2 - corner_radius, x1, y1 + corner_radius, **kwargs)

    # Draw the arcs for rounded corners
    canvas.create_arc(x1, y1, x1 + corner_radius * 2, y1 + corner_radius * 2, start=90, extent=90, style=tk.ARC, **kwargs)
    canvas.create_arc(x2 - corner_radius * 2, y1, x2, y1 + corner_radius * 2, start=0, extent=90, style=tk.ARC, **kwargs)
    canvas.create_arc(x2 - corner_radius * 2, y2 - corner_radius * 2, x2, y2, start=270, extent=90, style=tk.ARC, **kwargs)
    canvas.create_arc(x1, y2 - corner_radius * 2, x1 + corner_radius * 2, y2, start=180, extent=90, style=tk.ARC, **kwargs)


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
    def show_edit_menu(self):
        pass
        
class Line(DrawingObject):
    def __init__(self, x1, y1, x2, y2, color,id):
        super().__init__()
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
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
    
    def edit(self):
        editor.edit_line()

    def set_color(self, color):
        editor.canvas.itemconfig(self.id,fill=color)
    

    def show_on_select(self):
        editor.canvas.itemconfig(self.id, fill="black")
        editor.canvas.itemconfig(self.id, dash=(5, 5))
        pass
    def show_properly(self):
        editor.canvas.itemconfig(self.id, dash=())
        # editor.canvas.itemconfig(self.id, dash=(5, 5))
        pass
   
    
    

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
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.color)
    def set_id(self, id):
        self.id = id
    def is_clicked(self, x, y):
        # Check if (x, y) is inside the rectangle
        pass
    def move(self, dx, dy):
        # print(self.id)
        editor.canvas.coords(self.id, self.x1 + dx, self.y1 + dy, self.x2 + dx, self.y2 + dy)
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy
    def show_on_select(self):
        # editor.canvas.itemconfig(self.id, fill="red")
        editor.canvas.itemconfig(self.id, dash=(5, 5))

        pass
    
    def edit(self):
        print("yes,gussing")
        editor.edit_line()
        # editor.edit_rect_corner()

    def set_color(self, color):
        editor.canvas.itemconfig(self.id,fill=color)
    
    def set_corner(self,corner):
        self.corner_style = corner
        # Delete the existing rectangle
        editor.canvas.delete(self.id)
        # Create a new rectangle with updated corner style
        self.id = draw_rounded_rectangle(editor.canvas, 100, 100, 200, 200, 20, fill="blue", outline="")


    def show_properly(self):
        # editor.canvas.itemconfig(self.id, fill="red")
        # editor.canvas.itemconfig(self.id, dash=(5, 5))
        editor.canvas.itemconfig(self.id, dash=())
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





current_rectangle = None
current_line = None
choice = 'draw'
start_x, start_y = 0, 0 








class DrawingEditor:
    global canvas
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()
        self.objects = []
        self.selected_object = False
        
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
        global list_of_selected

        # Deselect the currently selected object
        if self.selected_object:
            for obj in list_of_selected:
                obj.show_properly()
            self.selected_object = False
            choice = 'draw'
            destroy_button_by_text(self.root, "group")
            destroy_button_by_text(self.root, "move")
            destroy_button_by_text(self.root, "line_edit_button")
            list_of_selected.clear()
            print('idhr khaali kr di h ', list_of_selected)
            return 
        
        # Select the new object
        self.selected_object = True
        self.create_rectangle()
        choice = 'select'
        self.canvas.button = tk.Button(root, text="group", command=self.remove_rectangle)
        self.canvas.button.pack()
        self.canvas.button = tk.Button(root, text="move", command=self.move_object)
        self.canvas.button.pack()
      
      
    def edit_line(self):
    # Create a button for selecting line color
        print("efone")
        # self.color_button = tk.Button(self.root, text="line_edit_button", command=self.show_color_options)
        # self.color_button.pack()
        self.corner_button = tk.Button(self.root, text="Corner_style_change", command=self.show_corner_options)
        self.corner_button.pack()


    def show_color_options(self):
        # Create a popup menu for selecting line color
        self.color_menu = tk.Menu(self.root, tearoff=0)
        self.color_menu.add_command(label="Black", command=lambda: self.change_line_color("black"))
        self.color_menu.add_command(label="Red", command=lambda: self.change_line_color("red"))
        self.color_menu.add_command(label="Green", command=lambda: self.change_line_color("green"))
        self.color_menu.add_command(label="Blue", command=lambda: self.change_line_color("blue"))
        
        # Display the color options menu
        self.color_menu.post(self.color_button.winfo_rootx(), self.color_button.winfo_rooty() + self.color_button.winfo_height())

    def change_line_color(self, color):
        # Change the color of the selected line(s)
        global list_of_selected
        for obj in list_of_selected:
            if isinstance(obj, Line):
                obj.set_color(color)
            if isinstance(obj,Rectangle):
                obj.set_color(color)

        # Redraw the canvas to reflect the color changes
        # self.redraw_canvas()
    
    
    # def edit_rect_corner(self):
    #     self.color_button = tk.Button(self.root, text="Corner_style_change", command=self.show_corner_options)
    #     self.color_button.pack()
    
    
    def show_corner_options(self):
        # Create a popup menu for selecting line color
        self.corner_menu = tk.Menu(self.root, tearoff=0)
        self.corner_menu.add_command(label="Square", command=lambda: self.change_corner("Square"))
        self.corner_menu.add_command(label="Rounded", command=lambda: self.change_corner("Rounded"))
        
        # Display the color options menu
        self.corner_menu.post(self.corner_button.winfo_rootx(), self.corner_button.winfo_rooty() + self.corner_button.winfo_height())
    
    
    def change_corner(self, corner):
        # Change the color of the selected line(s)
        global list_of_selected
        for obj in list_of_selected:
            if isinstance(obj,Rectangle):
                obj.set_corner(corner)

        # Redraw the canvas to reflect the color changes
        # self.redraw_canvas()
    
    
    
    
    def change_line_color(self, color):
        # Change the color of the selected line(s)
        global list_of_selected
        for obj in list_of_selected:
            if isinstance(obj, Line):
                obj.set_color(color)
            if isinstance(obj,Rectangle):
                obj.set_color(color)

        # Redraw the canvas to reflect the color changes
        # self.redraw_canvas()
    
    
        
    def move_object(self):
        print('yes')
        self.canvas.bind("<Button-1>",  self.start_move)
        self.canvas.bind("<B1-Motion>", self.move_object1)
        self.canvas.bind("<ButtonRelease-1>", self.end_move1)
        # self.canvas.unbind("<Button-1>")
        # self.canvas.unbind("<B1-Motion>")
        # self.canvas.unbind("<ButtonRelease-1>")
        
        
    def start_move(self, event):
        global start_x, start_y
        start_x, start_y = event.x, event.y
    def move_object1(self, event):
        global start_x, start_y
        global list_of_selected
        
        x, y = event.x, event.y
        dx, dy = x - start_x, y - start_y
        print('idhr h list_of_selected')
        print(list_of_selected)
        for obj in list_of_selected:
            
            if type(obj)==Group:
                for obj1 in obj.objects:
                    if type(obj1)==Rectangle:
                        obj1.move(dx, dy)
                    if type(obj1)==Line:
                        obj1.move(dx, dy)
            else:
                obj.move(dx, dy)
                
        start_x, start_y = x, y
        
    def end_move1(self, event):
        global choice
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        choice = 'draw'
        self.remove_rectangle()
        pass
    def remove_rectangle(self):
        # self.canvas.bind("<Button-1>", remove_rectangle)
        new_group = Group()
        global list_of_selected
        for obj in list_of_selected:
            print(obj)
            if isinstance(obj, Line):
                print('yes')
                list_of_lines.__delitem__(list_of_lines.index(obj))
            if isinstance(obj, Rectangle):
                print('yes1')
                list_of_rectangles.__delitem__(list_of_rectangles.index(obj))
            new_group.add_object(obj)
        list_of_groups.append(new_group)
        # list_of_selected.clear()
        
        # grp_obje = Group()
        #     # grp_obje.add_object(list_of_lines[-1])
        # for line in list_of_lines:
        #     # grp_obje.add_object(line)
        #     if line.x1 >= start_x and line.y1 >= start_y and line.x2 <= x and line.y2 <= y:
        #         grp_obje.add_object(line)
        #         list_of_lines.__delitem__(list_of_lines.index(line))
        # for rectangle in list_of_rectangles:
        #     if rectangle.x1 >= start_x and rectangle.y1 >= start_y and rectangle.x2 <= x and rectangle.y2 <= y:
        #         grp_obje.add_object(rectangle)
        #         list_of_rectangles.__delitem__(list_of_rectangles.index(rectangle))
        #         print
        # for group in list_of_groups:
        #     for obj in group.objects:
        #         if type(obj)==Line and obj.x1 >= start_x and obj.y1 >= start_y and obj.x2 <= x and obj.y2 <= y:
        #             grp_obje.add_object(group)
        #             break
        

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
        # print(f"Rectangle coordinates: ({start_x}, {start_y}) - ({x}, {y})")
        if choice == 'select':
            # editor.canvas.delete(current_line)
            grp_obje = Group()
            # grp_obje.add_object(list_of_lines[-1])
                    
            
            for line in list_of_lines:
                # grp_obje.add_object(line)
                if line.x1 >= start_x and line.y1 >= start_y and line.x2 <= x and line.y2 <= y:
                    # grp_obje.add_object(line)
                    list_of_selected.append(line)
                    # list_of_lines.__delitem__(list_of_lines.index(line))
            for rectangle in list_of_rectangles:
                if rectangle.x1 >= start_x and rectangle.y1 >= start_y and rectangle.x2 <= x and rectangle.y2 <= y:
                    # grp_obje.add_object(rectangle)
                    list_of_selected.append(rectangle)
                    # list_of_rectangles.__delitem__(list_of_rectangles.index(rectangle))
            for group in list_of_groups:
                for obj in group.objects:
                    if isinstance(obj,Line) and obj.x1 >= start_x and obj.y1 >= start_y and obj.x2 <= x and obj.y2 <= y:
                        list_of_selected.append(group)
                        break
                    elif isinstance(obj,Rectangle) and obj.x1 >= start_x and obj.y1 >= start_y and obj.x2 <= x and obj.y2 <= y:
                        list_of_selected.append(group)
                        break
            # list_of_selected.append(grp_obje)
            # list_of_selected.show_on_select()
            for obj in list_of_selected:
                print('yha kiya h show on select',obj)
                if(len(list_of_selected)==1):
                    if(isinstance(obj,Line)):
                        obj.edit()
                    if(isinstance(obj,Rectangle)):
                        obj.edit()
                obj.show_on_select()
            editor.canvas.delete(current_rectangle)
            
            return
        list_of_rectangles.append(Rectangle(start_x, start_y, x, y, "black", "sharp", id=current_rectangle))
def remove_rectangle(event):
    global current_rectangle
    if current_rectangle and choice == 'select':
        canvas.delete(current_rectangle)
        current_rectangle = None
        choice = 'draw'
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

# print(list_of_groups)
print('gopal')
print(list_of_lines)
print('list of rectangles')
print(list_of_rectangles)
print('list of groups')
for group in list_of_groups:
    print('new_group')
    print(group)