from expyriment import design, control, stimuli
#control.set_develop_mode()

exp = design.Experiment(name = "twoSquare")

control.initialize(exp)

def launching_function(temporal_time = 0, spatial_gap = 0, faster = False):
    '''the parameters in this function:
    temporal_time: the delays(ms) between red stopping and green starting
    spatial_gap: the distance(px) between the two squares
    faster: if True, the green square moves 3 times faster than the red one'''

    #initial
    square_size = (50, 50) #square size
    left_square = stimuli.Rectangle(size=square_size,colour= (255, 0, 0), position=(-400, 0)) #set colours and initial positions 
    right_square = stimuli.Rectangle(size = square_size, colour = (0, 255, 0), position = (0, 0))

    #for red square
    step_size_red = 5       # distance for each movement
    frame_delay = 10    # 10ms stop for each stop
    total_distance = 350 #total distance = 400-50 = 5 * 70
    n_steps_red = (total_distance - spatial_gap) // step_size_red     # total steps of red square

    #for green square
    step_size_green = 5 if not faster else step_size_red * 3
    n_steps_green = total_distance // step_size_green

    for i in range(n_steps_red):
    
        left_square.move((step_size_red, 0))#move the red square

    
        left_square.present(clear=True, update=False)  #draw left square without updating screen
        right_square.present(clear=False, update=True)  #draw tight square, update screen

        exp.clock.wait(frame_delay) #control the moving speed
    #temporal time
    if temporal_time > 0:
        exp.clock.wait(temporal_time)

    #red square reaches the green square, green square moves to the right
    for i in range(n_steps_green):
    
        right_square.move((step_size_green, 0))

    
        right_square.present(clear=True, update=False)   
        left_square.present(clear=False, update=True)  

        exp.clock.wait(frame_delay)

    exp.clock.wait(1000) #Show this display for 1 second.
    exp.screen.clear()
    exp.screen.update()

#test
control.start()

# Michottean launching
#launching_function(temporal_time= 0, spatial_gap= 0, faster = False)

# Temporal gap
#launching_function(temporal_time= 1000, spatial_gap= 0, faster = False)

# Spatial gap
#launching_function(temporal_time= 0, spatial_gap= 200, faster = False)

#faster
launching_function(temporal_time=0, spatial_gap=0, faster= True)

# Leave it on-screen until a key is pressed
exp.keyboard.wait()


# End the current session and quit expyriment
control.end()