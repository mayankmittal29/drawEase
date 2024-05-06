# Properties of the Design 

- In our design for the drawing editor application, we aimed for a balance among several key principles of good software design.

- Low Coupling: We ensured that the classes in my design are loosely coupled. For example, the DrawingEditor class interacts with Line, Rectangle, and Group objects through their common interface DrawingObject. This loose coupling allows for easier modification and maintenance of the code.

- High Cohesion: Each class in our design has a clear and single responsibility. For example, the Line class is responsible for representing a line object and defining its behavior. This high cohesion improves the readability and maintainability of the code.

- Separation of Concerns: We separated different concerns into different classes. For example, the DrawingObject class defines generic behavior common to all drawing objects, while the Line and Rectangle classes define behavior specific to lines and rectangles, respectively. This separation makes the code more modular and easier to understand.

- Information Hiding: We encapsulated the internal state of objects and exposed only necessary interfaces. For example, the Line class encapsulates the coordinates of the line (x1, y1, x2, y2) and exposes methods to manipulate them (move, is_clicked, delete, etc.). This information hiding improves the maintainability of the code by preventing direct access to internal state.

- Law of Demeter: We adhered to the Law of Demeter by limiting the interactions between objects to only immediate collaborators. For example, the DrawingEditor class interacts with Line, Rectangle, and Group objects through their common interface DrawingObject, rather than directly accessing their internal state. This reduces the coupling between classes and makes the code more maintainable.

- Extensibility: We ensured that our design allows for easy extension by adding new types of drawing objects or editor functionalities. For example, to add a new type of drawing object, you can simply create a new class that inherits from DrawingObject and implements its methods. This makes the code more flexible and adaptable to future changes.

- Reusability: Our design promotes reusability by defining common interfaces (DrawingObject) and behaviors (move, delete, etc.) that can be reused across different types of drawing objects. This reduces code duplication and improves maintainability.


# How I accomodated all points of Flexibility in my design

1. New primitive drawing object (eg. ellipse)

- for doing this we just need to create a new class and inherit DrawingObject class in this class.

2. Adding new operations on the drawing objects (eg. rotate)

- we just need to add a new functions in the DrawingObject class, Group class and all other shape's class.

3. Adding or replacing editors for new and existing object types (e.g., line style).

- 

4. New save or export file formats (e.g., JPEG)

- Standard code format is ascii code as we just need to write a function which converts ascii into the required format. 


Overall, We believe that my design demonstrates a good balance among these competing criteria, making it well-structured and able to accommodate future changes and product evolution.