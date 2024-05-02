<h1>Drawing Editor Project</h1>

This project is a prototype of a drawing editor application that allows users to create, manipulate, and save drawings consisting of various primitive shapes and objects. The design and implementation focus on extensibility and flexibility to accommodate future enhancements and modifications.
Features

    Drawing Object Types
        Supports indefinite drawing object types including lines, rectangles, and easily extensible to incorporate additional types like curves, ellipses, text, and images.

    Manipulating Objects
        Users can select, delete, copy, move, and edit objects in the drawing.
        Potential for adding operations like expand, shrink, rotate, etc., in the future.

    Editing Objects
        Objects provide a dialog box to edit properties (e.g., color, corner style for rectangles).

    Grouping Objects
        Objects can be grouped into larger units with nested grouping capabilities.
        Grouped objects can be manipulated collectively (e.g., move, copy, delete).

    Saving and Restoring Drawings
        Allows users to save drawings to a file in a custom ASCII text format.
        Supports opening and displaying drawings from saved files.
        Provides warning prompts to prevent data loss.

    Export to XML
        Offers XML export functionality for interoperability with other applications.

    Key Points of Flexibility
        Designed to accommodate new primitive drawing object types.
        Supports adding new operations on drawing objects.
        Allows addition or replacement of editors for existing or new object types.
        Enables integration of new save or export file formats.

File Format

The drawing file format uses a custom ASCII text format and supports grouping using begin and end markers. Primitive objects (lines, rectangles) and groups are defined in a structured manner.
Requirements and Limitations

    The canvas size is set to at least 400x400 pixels.
    Primitives within the drawing can be rendered in an arbitrary order without depth ordering.

Usage

    Installation
        Clone the repository to your local machine.

    Running the Program
        Launch the drawing editor application.
        Use the menu or toolbar buttons to perform drawing, object manipulation, and file operations.

    Creating Drawings
        Select an object type (line or rectangle) from the menu or toolbar.
        Use the mouse to draw the selected object on the canvas.

    Manipulating Objects
        Select objects by clicking on them.
        Perform operations (delete, copy, move, edit) using menu options or toolbar buttons.

    Saving and Loading Drawings
        Use the Save and Open operations from the menu or toolbar to save and load drawings.
        Provide file names for saving or specify a file name as a command-line argument for loading.

    Exporting to XML
        Export drawings to XML format using the appropriate menu option.

Future Enhancements

    Implement additional drawing object types (e.g., ellipses).
    Extend operations on drawing objects (e.g., rotation).
    Introduce new editors for existing or new object types (e.g., line style).
    Support new save or export file formats (e.g., JPEG).

<h3>Contributors</h3>
Mayank Mittal <br>
Divyaraj Mahida<br>
Shivam Mittal<br>
Gopal Garg<br>
