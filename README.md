# Py-Paint
Simple paint application on python-pygame.

## Requirements
pygame: Graphics platform (pip install pygame)
Currently requires a mouse with center wheel. Requirement will be removed in future.

## Usage
Run `paint.py`, pygame window will open upon running  
*Left-Click* - select pen-color and drawing  
*Right-Click* - select fill-color and filling screen  
*Center-Wheel* - reset screen (white background, cleared canvas)

## Contents
`paint.py:` Main loop and functions for drawing/updating window. 
`consts.py:` Contains constant definitions (colors, screensize, pensize).
`button.py:` Contains Button class (for color selection). Handles color changes and drawing buttons on main window.  

## Video Demonstration
Coming soon....

## Future Updates
- Organized menu to change pen-size and color
- Buttons for clearing the canvas (currently using mouse bindings)
- File Saving and Opening