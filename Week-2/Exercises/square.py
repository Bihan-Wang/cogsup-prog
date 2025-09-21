from expyriment import design, control, stimuli
#control.set_develop_mode()

exp = design.Experiment(name = "Square")

control.initialize(exp)

fixation = stimuli.FixCross()

# Create a 50 lenth square
square = stimuli.Rectangle(size=(50, 50), colour=(0, 0, 255))

# Start running the experiment
control.start(subject_id=1)

# Present the fixation cross and square
square.present(clear=True, update=False)
fixation.present(clear=False, update=True)

# Leave it on-screen for 500 ms
exp.clock.wait(500)

# Now display only the square (without fixation)
square.present(clear=True, update=True)


# Leave it on-screen until a key is pressed
exp.keyboard.wait()

# End the current session and quit expyriment
control.end()