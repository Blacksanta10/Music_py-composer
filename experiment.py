from Demo_music import *
from musicpy import *

#Idk what this is lol

#C major chord example
# Cmaj7 = chord(['C5','E5', 'G5', 'B5'])
# play(Cmaj7, wait=True, save_as_file=False)

# melody = chord('C5, C5, G5, G5, A5, A5, G5, F5, F5, E5, E5, D5, D5, C5',
#                 duration=[1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/4, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/4],
#                 interval=[1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/4, 1/8, 1/8, 1/8, 1/8, 1/8, 1/8, 1/4])
# play(melody, save_as_file=False, wait=True, bpm=80)

#Optimal syntax for writing chords    note[duration; interval; volume]
# r[duration] is used to for rests
# example = chord('G5[3/4;3/4], F5[.8;.8], r[.2], E5[.8;.8], F5[3/4;3/4], E5[.8;.8], D5[.8;.8], E5[.4;.4], D5[.4;.4], C5[.2;.2], B4[.4;.4], G4[.2;.2]')


#Scale is just data, not a playable phrase

# a = get_chord('C', 'maj7', intervals=1, duration=2)
# play(a, 150, i='Violin', save_as_file=False, wait=True)

# a = chord(['C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5', 'C6']) % (1/8,1/8)
# #a.pitch_bends.append(pitch_bend(value=30, start_time=3/8))
# play(a, 80,wait=True)

#testing
play_zanarkand()

