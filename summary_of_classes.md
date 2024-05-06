# Summary of classes 

## Line:

- Draw: Render the line on the canvas based on its properties such as coordinates, color, and dash offset.

- Set and Retrieve Properties: Allow setting and getting properties like ID, coordinates (start and end points), color, and dash offset.

- Handle Mouse Interactions: Respond to mouse events such as click, move, and delete to enable user interaction with the line object.

## Rectangle:

- Draw: Render the rectangle on the canvas based on its properties such as coordinates, color, corner style, and dash offset.

- Set and Retrieve Properties: Allow setting and getting properties like ID, coordinates (top-left and bottom-right corners), color, corner style, and dash offset.

- Handle Mouse Interactions: Respond to mouse events such as click, move, and delete to enable user interaction with the rectangle object.

## Group:

- Manage Drawing Objects: Maintain a list of drawing objects within the group to organize and manipulate them collectively.

- Add, Draw, and Delete Objects: Provide functionality to add objects to the group, draw them on the canvas, and remove them from the group when needed.

- Handle Mouse Interactions: Respond to mouse events to enable selection, movement, and interaction with objects within the group.

- Ungroup Objects: Allow breaking the group apart to separate individual objects for independent manipulation.

## DrawingObject:

- Common Behaviors: Define common functionalities shared by all drawing objects, such as handling mouse clicks, moving objects, deleting objects, and copying objects.

- Draw: Implement the drawing method to render the object on the canvas with proper rendering.

- Show Proper Rendering: Ensure that the object is displayed correctly on the canvas according to its properties and state.

## DrawingEditor:

- Manage User Interface: Handle user interactions and manage UI components like menus, toolbars, and canvas.

- Create and Manipulate Objects: Provide methods for creating new drawing objects (lines, rectangles), editing existing objects, and managing object selection.

- File Operations: Support functionalities for opening, saving, and loading drawing files.

- Generate Code: Generate code based on the current drawing for further processing or exporting.

- Handle Mouse Events: Respond to mouse events such as clicks, drags, and releases to enable interactive drawing and editing.