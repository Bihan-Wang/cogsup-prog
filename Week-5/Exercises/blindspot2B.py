from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
#control.set_develop_mode() 
control.initialize(exp)

exp.add_data_variable_names(["side", "key_pressed", "radius", "x_coord", "y_coord"])
#to match the code of keyboard with their meaning
key_map = {
    K_UP: "up",
    K_DOWN: "down",
    K_LEFT: "left",
    K_RIGHT: "right",
    K_SPACE: "space",
    ord('1'): "smaller",
    ord('2'): "bigger"
}

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial(side):
    # different positions according to the eye
    if side == 'R':
        instructions_text = "Cover your left eye.\n\n Fixate on the cross.\n\n Use ARROWS to move the circle.\n Press '1' to make it smaller, '2' to make it larger.\n\n Press SPACE when done."
        fixation_pos = [-300, 0]
        circle_start_pos = [0, 0]
    else: # 'L'
        instructions_text = "Cover your right eye.\n\n Fixate on the cross.\n\n Use ARROWS to move the circle.\n Press '1' to make it smaller, '2' to make it larger.\n\n Press SPACE when done."
        fixation_pos = [300, 0]
        circle_start_pos = [0, 0]

    
    instructions = stimuli.TextScreen("instructions", instructions_text)
    instructions.present()
    exp.keyboard.wait() 

    
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=fixation_pos)
    fixation.preload()

    radius = 75
    circle = make_circle(radius, pos=circle_start_pos)
    move_step = 5

   
    while True:
        exp.screen.clear()
        fixation.present(clear=False, update=False)
        circle.present(clear=False, update=True)

        key = exp.keyboard.check()

        
        # If a key was pressed, log the data.
        if key is not None:
            
            key_name = key_map.get(key, str(key))
            
            current_x = circle.position[0]
            current_y = circle.position[1]

            
            exp.data.add([side, key_name, radius, current_x, current_y])

            if key == K_UP:
                circle.move((0, move_step))
            elif key == K_DOWN:
                circle.move((0, -move_step))
            elif key == K_LEFT:
                circle.move((-move_step, 0))
            elif key == K_RIGHT:
                circle.move((move_step, 0))
            elif key == ord('1'): 
                radius = max(5, radius - move_step)
                circle = make_circle(radius, circle.position)
            elif key == ord('2'):
                radius = radius + move_step
                circle = make_circle(radius, circle.position)
            elif key == K_SPACE:
                break 


control.start(subject_id=1)

run_trial(side='R')
run_trial(side='L')

control.end()