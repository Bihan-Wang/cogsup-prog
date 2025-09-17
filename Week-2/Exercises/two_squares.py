from expyriment import design, control, stimuli
square_size = (50, 50)
left_square = stimull.Rectangle(size=square_size,colour= (8, 8, 255), position=(-108, 6))
right_square = stimuli.Rectangle(size = square_size, colour = (0, 255, 0), position = (108,6))
left_square.present(clear = True, update = False)
right_square.present(clear=False, update=True)