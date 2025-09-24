
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY

control.set_develop_mode() 

exp = design.Experiment(name="Kanizsa Square", background_colour= C_GREY)
control.initialize(exp)

#size of screen
width, height = exp.screen.size 

#size of sqaure and circle
size_sqaure = int(width * 0.25)
R_circle = int(width * 0.05)

#positions of circles
positions_C_black = [ (-size_sqaure // 2, size_sqaure //2),
              (size_sqaure // 2, size_sqaure //2)]
positions_C_white = [ (-size_sqaure // 2, -size_sqaure //2),
              (size_sqaure // 2, -size_sqaure //2)]

circles_black = [
    stimuli.Circle(radius= R_circle, position=pos, colour=(255, 255, 255))
    for pos in positions_C_black
]

square = stimuli.Rectangle(size=(size_sqaure, size_sqaure), position=(0, 0), colour=C_GREY)

control.start()

# 
for c in circles_black:
    c.present(clear=False, update=False)

# 
square.present(clear=False, update=False)


exp.screen.update()


exp.keyboard.wait()
control.end()
