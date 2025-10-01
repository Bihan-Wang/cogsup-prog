from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")

#control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
square = stimuli.Rectangle(size=(100, 100), line_width=5)


stims = [fixation, square]
def draw(stims):
    exp.screen.clear()
    for stim in stims:
        stim.present(clear = False, update= False)
    exp.screen.update()

control.start(subject_id=1)

fixation.present(clear=True, update=True)

exp.clock.wait(500)

#square.present(clear=False, update=False)
draw(stims)
exp.keyboard.wait()

control.end()