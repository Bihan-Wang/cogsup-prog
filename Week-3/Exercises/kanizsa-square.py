
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY

#control.set_develop_mode() 

exp = design.Experiment(name="Kanizsa Square", background_colour= C_GREY)
control.initialize(exp)

#size of screen
width, height = exp.screen.size 

#size of sqaure and circle
size_sqaure = int(width * 0.25)
R_circle = int(width * 0.05)


circle_black1= stimuli.Circle(radius= R_circle, position=(-size_sqaure // 2, size_sqaure //2), colour=(0, 0, 0))
circle_black2= stimuli.Circle(radius= R_circle, position=(size_sqaure // 2, size_sqaure //2), colour=(0, 0, 0))
circle_white1= stimuli.Circle(radius= R_circle, position=(-size_sqaure // 2, -size_sqaure //2), colour=(255, 255, 255))
circle_white2= stimuli.Circle(radius= R_circle, position=(size_sqaure // 2, -size_sqaure //2), colour=(255, 255, 255))

square = stimuli.Rectangle(size=(size_sqaure, size_sqaure), position=(0, 0), colour=C_GREY)

control.start()


circle_black1.present(clear=True, update=False)
circle_black2.present(clear = False, update = False)
circle_white1.present(clear = False, update = False)
circle_white2.present(clear = False, update = False)

square.present(clear=False, update=True)




exp.keyboard.wait()
control.end()
