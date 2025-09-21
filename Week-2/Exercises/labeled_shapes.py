
import math
from expyriment import design, control, stimuli
from expyriment.misc import geometry

#control.set_develop_mode()
control.defaults.window_mode = True

exp = design.Experiment("Polygon")
control.initialize(exp)

# the triangle
triangle = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(3, 50), colour=(128, 0, 128))  # 紫色
triangle.position = (-150, 0)  # the position of the triangle

# the hexagon
R_hex = 50 / math.sqrt(3) #the side of hexagon
hexagon = stimuli.Shape(vertex_list=geometry.vertices_regular_polygon(6, R_hex), colour = (255,255,0))
hexagon.position = (150, 0)

# the vertical line (50px-long and 3px-wide, white)
vertical_line1 = stimuli.Line(
    (0, -25),  # start point
    (0,  25),  # end point
    line_width=3,
    colour=(255, 255, 255)  # 白色
)

vertical_line2 = stimuli.Line(
    (0, -25),  # start point
    (0,  25),  # end point
    line_width=3,
    colour=(255, 255, 255)  # 白色
)

vertical_line1.position = (-150, 50) # at the top of each shape
vertical_line2.position = (150, 50)

# the labels
label_tri = stimuli.TextLine(
    "triangle",
    text_colour=(255, 255, 255),  # white
    text_size=20,                 # the size of letters
    text_font="Arial"             
)

label_hex = stimuli.TextLine(
    "hexagon",
    text_colour=(255, 255, 255),  # white
    text_size=20,                 # the size of letters
    text_font="Arial"             
)

label_tri.position = (-150,100)
label_hex.position = (150,100) # at the top of the vertical lines

#present all elements
control.start()
triangle.present(clear=True, update=False)  
hexagon.present(clear = False, update= False)
vertical_line1.present(clear = False, update = False)
vertical_line2.present(clear = False, update = False)
label_tri.present(clear= False, update= False)
label_hex.present(clear = False, update = True)
# Leave it on-screen until a key is pressed
exp.keyboard.wait()


# End the current session and quit expyriment
control.end()