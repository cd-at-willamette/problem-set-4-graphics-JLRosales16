############################################################
# Name:Jacob Rosales
# Name(s) of anyone worked with:
# Est time spent (hr):
############################################################

from pgl import GWindow, GRect, GOval

# Setting up initial window dimensions. 
WIDTH = 600
HEIGHT = 600

from pgl import GWindow, GRect, GOval, GLine, GLabel

def draw_beautiful_scene():
    # Create a window for the drawing
    window = GWindow(500, 400)

    # Draw the ground (GRect)
    ground = GRect(0, 300, 500, 100)
    ground.setFilled(True)
    ground.setColor("green")
    window.add(ground)

    # Draw the sun (GOval)
    sun = GOval(400, 20, 80, 80)
    sun.setFilled(True)
    sun.setColor("yellow")
    window.add(sun)

    # Draw a tree trunk (GRect)
    trunk = GRect(120, 250, 20, 50)
    trunk.setFilled(True)
    trunk.setColor("brown")
    window.add(trunk)

    # Draw tree foliage (GOval)
    foliage = GOval(100, 200, 60, 60)
    foliage.setFilled(True)
    foliage.setColor("darkgreen")
    window.add(foliage)

    # Draw a ray of sunlight (GLine)
    sun_ray = GLine(440, 60, 300, 200)
    sun_ray.setColor("orange")
    window.add(sun_ray)

    # Add a label to the scene (GLabel)
    label = GLabel("A Peaceful Day", 180, 380)
    label.setFont("Serif-20")
    window.add(label)

# Call the function to draw the scene
draw_beautiful_scene()


if __name__ == '__main__':
    # Create one GWindow instance and pass it to both functions
    gw = GWindow(WIDTH, HEIGHT)
    draw_image(gw)
    add_oval(gw)
