from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK
control.set_develop_mode()
def hermann_grid(square_size, square_colour,
                 spacing , rows, cols,
                 background_colour):

    exp = design.Experiment("Hermann Grid", background_colour=C_WHITE)
    control.initialize(exp)

    # total width and height 
    total_width = cols * square_size + (cols - 1) * spacing
    total_height = rows * square_size + (rows - 1) * spacing

    
    canvas = stimuli.BlankScreen(colour=background_colour)

    
    for i in range(rows):
        for j in range(cols):
            x = -total_width/2 + j * (square_size + spacing) + square_size/2
            y =  total_height/2 - i * (square_size + spacing) - square_size/2
            square = stimuli.Rectangle(size=(square_size, square_size),
                                       position=(x, y),
                                       colour=square_colour)
            square.plot(canvas)

    control.start()
    canvas.present()
    exp.keyboard.wait()
    control.end()



hermann_grid(square_size=80, spacing=10, rows=6, cols=6,
            square_colour=C_BLACK, background_colour=C_WHITE) #the illusion most depends on the space between each sqaure