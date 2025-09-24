from expyriment import design, control, stimuli


exp = design.Experiment("display_edge")
control.initialize(exp)

width, height = exp.screen.size

square_size = int(width * 0.05)

#position of the four point
positions = ([- width // 2 + square_size//2 , height // 2 - square_size//2],
             [width // 2 - square_size//2, height//2 - square_size//2],
             [-width // 2+ square_size//2, -height // 2 + square_size//2],
             [width // 2 -square_size//2, -height //2 + square_size//2])

squares =[ stimuli.Rectangle(size=(square_size,square_size), position= pos, colour=(255, 0, 0), line_width= 1) for pos in positions]

control.start()

for sq in squares:
    sq.present(clear=False, update=False)
exp.screen.update()


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()