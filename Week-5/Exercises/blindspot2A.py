from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_SPACE

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
control.initialize(exp)

# NEW CODE PART 1: Define Data Columns
exp.add_data_variable_names(["side", "final_radius", "final_x", "final_y"])

""" Stimuli """
def make_circle(r, pos=(0,0)):
    """A helper function to create and preload a circle"""
    c = stimuli.Circle(r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial(side):
    if side == 'R':
        instructions_text = "Please cover your left eye and fixate on the cross with your right eye.\n\nUse the arrow keys to move the circle until it disappears.\nUse '1' and '2' to adjust its size.\n\nPress [SPACE] when finished."
        fixation_pos = [-300, 0]
        circle_start_pos = [0, 0]
    else: # 'L'
        instructions_text = "Please cover your right eye and fixate on the cross with your left eye.\n\nUse the arrow keys to move the circle until it disappears.\nUse '1' and '2' to adjust its size.\n\nPress [SPACE] when finished."
        fixation_pos = [300, 0]
        circle_start_pos = [0, 0]

    instructions = stimuli.TextScreen("Instructions", instructions_text)
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

    #NEW CODE PART 2: Add Data for the Trial 
    # add one row to the data file with the final values 
    final_x = circle.position[0]
    final_y = circle.position[1]
    exp.data.add([side, radius, final_x, final_y])


control.start(subject_id=1)

run_trial(side='R')
run_trial(side='L')
    
control.end()