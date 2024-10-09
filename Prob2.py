########################################
# Name: Jacob Rosales
# Collaborators:
# Estimated time spent (hrs):1
########################################


from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15

def draw_pyramid():
    # Create the window for the drawing
    window = GWindow(500, 400)

    # Calculate the starting x and y coordinates for the base row
    window_width = window.getWidth()
    window_height = window.getHeight()
    
    # Calculate the total width of the base row
    pyramid_base_width = BRICKS_IN_BASE * BRICK_WIDTH
    start_x = (window_width - pyramid_base_width) / 2
    start_y = (window_height + BRICKS_IN_BASE * BRICK_HEIGHT) / 2

    # Loop through each row, starting from the base
    for row in range(BRICKS_IN_BASE):
        # Calculate the number of bricks in the current row
        bricks_in_row = BRICKS_IN_BASE - row

        # Calculate the starting x position for this row
        row_start_x = start_x + (row * BRICK_WIDTH / 2)

        # Loop through each brick in the current row
        for brick in range(bricks_in_row):
            x = row_start_x + brick * BRICK_WIDTH
            y = start_y - row * BRICK_HEIGHT

            # Create and add the brick to the window
            brick_rect = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
            brick_rect.setFilled(True)
            brick_rect.setColor("gray")
            window.add(brick_rect)

# Call the function to draw the pyramid
draw_pyramid()



















if __name__ == '__main__':
    draw_pyramid()
