import itertools
import random
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_r, K_b, K_g, K_o, K_SPACE

""" 1. Constants """
KEY_MAPPING = {"red": K_r, "blue": K_b, "green": K_g, "orange": K_o}
KEYS = list(KEY_MAPPING.values())
COLORS = ["red", "blue", "green", "orange"]

N_BLOCKS = 8
TOTAL_TRIALS = 128
N_TRIALS_IN_BLOCK = TOTAL_TRIALS // N_BLOCKS

INSTR_START = """
Welcome to the Stroop task!

A word will be displayed on the screen in a certain color.
Your task is to identify the COLOR of the word, ignoring what the word says.

Press the key corresponding to the first letter of the color:
'R' for Red
'B' for Blue
'G' for Green
'O' for Orange

Please respond as quickly and accurately as possible.\n
Press SPACE to begin.
"""
INSTR_MID = f"""You have completed a block. \n
Press SPACE to continue."""
INSTR_END = """You have completed the experiment. \n
Press SPACE to quit."""

FEEDBACK_CORRECT = stimuli.TextLine("Correct")
FEEDBACK_INCORRECT = stimuli.TextLine("Incorrect")

"""2. Helper functions """
def derangements(lst):
    ders = []
    for perm in itertools.permutations(lst):
        if all(original != p for original, p in zip(lst, perm)):
            ders.append(list(perm))
    return ders

def present_instructions(text):
    stimuli.TextScreen(text=text, text_justification=0, heading="Instructions").present()
    exp.keyboard.wait(K_SPACE)

""" 3. Global settings  """
exp = design.Experiment(name="Stroop (Balanced)", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['subject_id', 'block_id', 'trial_id', 'trial_type', 'word', 'color', 'correct_key', 'response_key', 'RT', 'correct'])
control.set_develop_mode()
control.initialize(exp)

fixation = stimuli.FixCross()
stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}

for w in COLORS:
    for c in COLORS:
        stims[w][c].preload()
fixation.preload()
FEEDBACK_CORRECT.preload()
FEEDBACK_INCORRECT.preload()

""" 4. Experiment  """
def run_trial(trial):
    stim = stims[trial["word"]][trial["color"]]
    fixation.present()
    exp.clock.wait(500)
    stim.present()
    key, rt = exp.keyboard.wait(keys=KEYS)
    correct = 1 if key == trial["correct_key"] else 0
    feedback = FEEDBACK_CORRECT if correct else FEEDBACK_INCORRECT
    feedback.present()
    exp.clock.wait(1000)
    exp.data.add([
        exp.subject, trial['block_id'], trial['trial_id'], trial['trial_type'],
        trial['word'], trial['color'], trial['correct_key'], key, rt, correct
    ])



control.start()


PERMS = derangements(COLORS)
order = (exp.subject - 1) % len(PERMS)
perm = PERMS[order]

base_trials = []
for color in COLORS:
    base_trials.append({
        "trial_type": "match", "word": color, "color": color,
        "correct_key": KEY_MAPPING[color]
    })
for word, color in zip(COLORS, perm):
    base_trials.append({
        "trial_type": "mismatch", "word": word, "color": color,
        "correct_key": KEY_MAPPING[color]
    })

block_repetitions = N_TRIALS_IN_BLOCK // len(base_trials)
all_trials = []
for b in range(1, N_BLOCKS + 1):
    block_trials = base_trials * block_repetitions
    random.shuffle(block_trials)
    for i, t in enumerate(block_trials, 1):
        t['block_id'] = b
        t['trial_id'] = i
        all_trials.append(t)


present_instructions(INSTR_START)

for i, trial in enumerate(all_trials):
    run_trial(trial)
    if (i + 1) % N_TRIALS_IN_BLOCK == 0 and (i + 1) < TOTAL_TRIALS:
        present_instructions(INSTR_MID)

present_instructions(INSTR_END)
control.end()