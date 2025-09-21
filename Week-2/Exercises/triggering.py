from expyriment import design, control, stimuli
#control.set_develop_mode()

exp = design.Experiment(name = "twoSquare")

control.initialize(exp)

#initial
square_size = (50, 50) #square size
left_square = stimuli.Rectangle(size=square_size,colour= (255, 0, 0), position=(-400, 0)) #set colours and initial positions 
right_square = stimuli.Rectangle(size = square_size, colour = (0, 255, 0), position = (0, 0))


#movement for red square
step_size1 = 5       # distance for each movement
frame_delay = 10    # 10ms for each stop
n_steps1 = 70        # total steps = 400-50

control.start()

for i in range(n_steps1):
    
    left_square.move((step_size1, 0))#move the red square

    
    left_square.present(clear=True, update=False)  #draw left square without updating screen
    right_square.present(clear=False, update=True)  #draw tight square, update screen

    exp.clock.wait(frame_delay) #control the moving speed

#movement for green square
step_size2 = 15    # 3 times faster than red square
n_steps2 = 23    #total steps = 350, about 15 *23

#red square reaches the green square, green square moves to the right
for i in range(n_steps2):
    
    right_square.move((step_size2, 0))

    
    right_square.present(clear=True, update=False)   
    left_square.present(clear=False, update=True)  

    exp.clock.wait(frame_delay)

exp.clock.wait(1000) #Show this display for 1 second.
exp.screen.clear()
exp.screen.update()
# Leave it on-screen until a key is pressed
exp.keyboard.wait()


# End the current session and quit expyriment
control.end()