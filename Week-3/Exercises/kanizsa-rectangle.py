from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY

def kanizsa_rectangle(aspect_ratio, rect_scale, circle_scale):
    
    exp = design.Experiment("Kanizsa Rectangle", background_colour=C_GREY)
    control.initialize(exp)

    # screen size
    w, h = exp.screen.size

    # rectangle size
    rect_width = int(w * rect_scale) #rectangle width relative to screen width
    rect_height = int(rect_width / aspect_ratio) #width/height ratio of rectangle

    # circle radius
    R_circle = int(w * circle_scale) #circle radius relative to screen width

    

    circle_black1= stimuli.Circle(radius= R_circle, position=(-rect_width // 2,  rect_height // 2), colour=(0, 0, 0))
    circle_black2= stimuli.Circle(radius= R_circle, position=(rect_width // 2,  rect_height // 2), colour=(0, 0, 0))
    circle_white1= stimuli.Circle(radius= R_circle, position=(-rect_width // 2,  -rect_height // 2), colour=(255, 255, 255))
    circle_white2= stimuli.Circle(radius= R_circle, position=(rect_width // 2,  -rect_height // 2), colour=(255, 255, 255))

    rect = stimuli.Rectangle(size=(rect_width, rect_height), position=(0,0), colour=C_GREY)

    control.start()

    # draw circles
    circle_black1.present(clear=True, update=False)
    circle_black2.present(clear = False, update = False)
    circle_white1.present(clear = False, update = False)
    circle_white2.present(clear = False, update = False)
    # draw rectangle
    rect.present(clear=False, update=True)

    exp.keyboard.wait()
    control.end()




kanizsa_rectangle(aspect_ratio=1.5, rect_scale=0.5, circle_scale=0.05)
