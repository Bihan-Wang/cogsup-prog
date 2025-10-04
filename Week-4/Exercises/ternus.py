import expyriment
from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE, C_WHITE, C_RED, C_GREEN, C_YELLOW

control.set_develop_mode()
exp = design.Experiment(name="Ternus Display")
control.initialize(exp)

FRAME_DURATION = 10           
CIRCLE_RADIUS  = 30
TAG_RADIUS     = 5
TAG_OFFSET     = (0, 0)

POSITIONS_A = [(-100, 0), (0, 0), (100, 0)]
POSITIONS_B = [(0, 0), (100, 0), (200, 0)]

# for the color tags order
COLORS_A = [C_YELLOW, C_RED, C_GREEN]
COLORS_B = [C_RED, C_GREEN, C_YELLOW]

#control the present time
def present_for(stimuli_list, frames):
    duration_ms = frames * (1000 / 60.0)
    if duration_ms <= 0:
        return
    t0 = exp.clock.time

    exp.screen.clear()
    if stimuli_list:
        stimuli_list[0].present(clear=False, update=False)
        for stim in stimuli_list[1:]:
            stim.present(clear=False, update=False)
    exp.screen.update()

    draw_time = exp.clock.time - t0
    remain = duration_ms - draw_time
    if remain > 0:
        exp.clock.wait(remain)


def make_circles(positions, radius, color):
    circles = [stimuli.Circle(radius=radius, position=pos, colour=color) for pos in positions]
    for c in circles:
        c.preload()
    return circles


def add_tags(positions, offset, tag_radius, tag_colors):
    tags = []
    for (x, y), color in zip(positions, tag_colors):
        tx, ty = x + offset[0], y + offset[1]
        t = stimuli.Circle(radius=tag_radius, position=(tx, ty), colour=color)
        t.preload()
        tags.append(t)
    return tags


def run_trial(isi_frames, use_tags):# display the information of parameters
    exp.screen.clear()
    exp.screen.update()
    info = stimuli.TextLine(
        f"ISI = {isi_frames} frames. Tags = {use_tags}. Press SPACE to continue.",
        position=(0, -200)
    )
    info.preload()
    info.present()
    exp.clock.wait(1000)

   
    circles_A = make_circles(POSITIONS_A, CIRCLE_RADIUS, C_WHITE)
    circles_B = make_circles(POSITIONS_B, CIRCLE_RADIUS, C_WHITE)

    if use_tags:
        tags_A = add_tags(POSITIONS_A, TAG_OFFSET, TAG_RADIUS, COLORS_A)
        tags_B = add_tags(POSITIONS_B, TAG_OFFSET, TAG_RADIUS, COLORS_B)
        stims_A = circles_A + tags_A
        stims_B = circles_B + tags_B
    else:
        stims_A = circles_A
        stims_B = circles_B

    while True:
        if exp.keyboard.check(K_SPACE):
            break
        present_for(stims_A, FRAME_DURATION)
        present_for([], isi_frames)
        present_for(stims_B, FRAME_DURATION)
        present_for([], isi_frames)

    exp.screen.clear()
    exp.screen.update()
    exp.clock.wait(200)


# Low ISI without color tag 
run_trial(isi_frames=1,  use_tags=False)
# High ISI without color tag
run_trial(isi_frames=12, use_tags=False)
# high ISI with color tag
run_trial(isi_frames=12, use_tags=True)

control.end()