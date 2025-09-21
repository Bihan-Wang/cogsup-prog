from expyriment import design, control, stimuli
#control.set_develop_mode()

exp = design.Experiment(name = "twoSquaremove")

control.initialize(exp)


square_size = (50, 50)
left_square = stimuli.Rectangle(size=square_size,colour= (255, 0, 0), position=(-100, 0))
right_square = stimuli.Rectangle(size = square_size, colour = (0, 255, 0), position = (100, 0))
left_square.present(clear = True, update = False)
right_square.present(clear=False, update=True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()


# End the current session and quit expyriment
control.end()