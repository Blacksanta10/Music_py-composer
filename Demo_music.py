
# Use python version 3.10 in vscode
# These are examples of usign musicpy
# All of these Demos are from the documentation

import musicpy as mp
from musicpy import *


### Example 1: play broken chords on chord progression
def play_broken_chords():
    guitar = (C('CM7', 3, 1/4, 1/8)^2 |
            C('G7sus', 2, 1/4, 1/8)^2 |
            C('A7sus', 2, 1/4, 1/8)^2 |
            C('Em7', 2, 1/4, 1/8)^2 | 
            C('FM7', 2, 1/4, 1/8)^2 |
            C('CM7', 3, 1/4, 1/8)@1 |
            C('AbM7', 2, 1/4, 1/8)^2 |
            C('G7sus', 2, 1/4, 1/8)^2) * 2
    play(guitar, bpm=100, instrument=25, wait=True, save_as_file=False)



### Example 2: Ethereal piano soundtrack
def play_ethereal_piano_sound():
    a = (C('G/C',3) @ [1,2,3,2,1.1,2,3,2]) % (2,1/8) | (2, 1)
    result = (a | 1 | a - 2) + database.octave
    result.other_messages = [
    event('control_change', control=10, value=0, start_time=0),
    event('control_change', control=10, value=127, start_time=2),
    event('control_change', control=10, value=64, start_time=4)
    ]
    play(result, 165, wait=True, save_as_file=False)


### Example 3: J-rock intro
def play_jrock_intro():
    guitar = ((C('Cmaj7')@1)@[1,2,3,4,1,2,3,2] |
    (C('Fmaj7',3)^2)@[1,2,3,4,1,2,3,2] |
    (C('G7sus',3)^2)@[1,2,3,4,1,2,3,2] |
    C('Am11',3)@[1,2,4,6,1,4,6,4] |
    (C('Cmaj7')@1)@[1,2,3,4,1,2,3,2] |
    C('Fadd9',3).up(2,1)@[1,2,3,4,1,2,3,2] |
    (C('G7sus',3)^2)@[1,2,3,4,1,2,3,2] |
    C('Am11',3)@[1,2,4,6,1,4,6,4]) % (1/2,1/8)
    guitar2 = (C('Am11',3)@[1,2,4,6,1,4,6,4] |
    (C('Em7',3)^2)@[1,2,3,4,1,2,3,2] |
    (C('Fmaj9',3)^2)@[1,2,3,4,1,2,3,2] |
    (C('Cmaj9')^2)@[1,2,3,4,1,2,3,2] |
    C('Am11',3)@[1,2,4,6,1,4,6,4] |
    (C('Em7',3)^2)@[1,2,3,4,1,2,3,2] |
    (C('Fmaj9',3)^2)@[1,2,3,4,1,2,3,2] |
    (C('Cmaj9')^2)@[1,2,3,4,1,2,3,2]) % (1/2,1/8)
    bass1 = chord('D2[.8;.],E2[.8;.],D2[.8;.],E2[1;.], F2[1;.], G2[1;.], A1[.2;.], A2[.8;.], G2[.8;.], E2[.8;.], D2[.8;.]')
    bass2 = (chord('E2')*8 + chord('F1')*8 + chord('G1')*8 + chord('A1,A1,E2,A1,A2,A1,G2,D2')) % (1/8,1/8) * 2
    bass3 = (chord('A2')*8 + chord('E2')*8 + chord('F2')*8 + chord('C2,C2,G2,C2,C3,C2,G2,C2')) % (1/8,1/8) * 2
    bass = bass1 | bass2 | bass3
    rhythm_guitar = (C('A5(+octave)',2, 1) | C('E5(+octave)',2, 1) | C('F5(+octave)',2, 1) | C('C5(+octave)',3, 1/2)| C('G5(+octave)',2, 1/2)) * 2
    string1 = chord('B5[1;.],C6[1;.],D6[.2;.],E6[.2;.],\
    F6[.2;.],E6[.2;.],C6[1;.],B5[.2;.],C6[.2;.],G5[1;.],\
    F5[.2;.],E5[.2;.],C5[1;.],D5[.4;.],E5[.4;.],F5[.4;.],\
    E5[.4;.],D5[.2;.],G5[.2;.],E5[1;.]')
    drum1 = drum('K, H, S, H, r:2, K, H, OH;S, H, K, H, S, H').notes
    drum1.set_volume(112)
    result = piece([guitar * 2 | guitar2, bass, string1, rhythm_guitar,drum1 * 4 + 2],
                [2, 34, 49, 31, 1],
                bpm=165,
                start_times=[0, 4-3/8, 12, 16, 16],
                channels=[0,1,2,3,9])
    play(result-2, wait=True, save_as_file=False)


### Example 4: Opening of Piano Nocturne
def play_piano_nocturne_op():
    w1 = ((C('Cmadd2') + 'C5') % (1/2,1/8) | 3/8 |
    (C('Cmadd2') + 'C5') % (1/2,1/8) | 3/8 |
    chord('F5,D#5,D5,D#5,C5') % (1/2,1/8))

    w2 = (C('G#add9',3) @ [1,3,1.1,4,2.1] % (1/2,1/8) | 3/8 |
    C('A#add9',3) @ [1,3,1.1,4,2.1] % (1/2,1/8) | 3/8 |
    (C('Cmadd9,add11',3) @ [1,3,1.1,4,2.1,5,2.1,4] % (1/2,1/8)) * 2)

    play((w1 & (w2, 1/2)) | (2, -7/8), 90, wait=True)  


## Example 5: Non- functional harmonic game bgm
def play_non_harmonic_game():
    a = C('Cm9',4,1/2,1/8) @ [1,3,5,2.1,4.1] | 3/8
    piano = a * 4 | (a + 3) * 4
    bass = (chord('C2, C2, G2, C2, A#2, C2, C3, C2') * 4) % (1/8, 1/8)
    bass += (bass + 3)
    import random
    drum = concat([chord(random.choice(['D2','E2','G2'])) for i in range(64)]) % (1/8, 1/8)
    play(P([piano, bass, drum], [1, 34, 1], 500, [0, 0, 0], channels=[1,2,9]) * 2, wait=True, save_as_file=False)


### Example 6: Rolling Star Yui
def play_rolling_star_yui():
    bass11 = translate('B1[l:.8; i:.; r:8], D2[l:.8; i:.; r:8], A1[l:.8; i:.; r:8], G1[l:.8; i:.; r:8]')
    bass12 = translate('G1[l:.8; i:.; r:6], A1[l:.8; i:.; r:2]')
    bass1 = bass11 * 2 | bass12

    guitar11 = translate('B3[l:.4; i:.], D4[l:.8; i:.], E4[l:3/8; i:.], D4[l:.8; i:.], E4[l:.8; i:.]')
    guitar12 = guitar11.down(2, 0)
    guitar13 = guitar12.down(1, [1, 3])
    guitar14 = translate('G3[l:.4; i:.], B3[l:.8; i:.], A4[l:5/8; i:.]')
    guitar1 = (guitar11|guitar12|guitar13|guitar14) * 2

    drum11 = drum('C;K, H, S, H | K, H, S, H, r:5, C;K, H;S[r:2], PH, OH, S;OH[r:3]').notes
    drum12 = drum('C;K;H;S, H;S[r:2], PH, OH, S;OH[r:3]').notes
    drum1 = drum11 * 2 | drum12

    synth11 = translate('D5[l:.8; i:.], B5[l:.8; i:.], r:16')
    synth1 = synth11

    result = P([bass1, guitar1, drum1, synth1],
            [34, 31, 1, 91],
            bpm=165,
            channels=[0,1,9,2],
            start_times=[0,0,0,4])

    play(result, wait=True, save_as_file=False)

    
#Zanarkand music score.

#Combo in measure 1
a = N('D6')
b = N('F#6')
D_Fsharp6 = a + b

#Combo in measure 2
b = N('E6')
c = N('G6')
B_F6 = b + c

#Rhythm for eight notes in 3/4 time signature
rhythm_eights = rhythm('b:1/8 b:1/8 b:1/8 b:1/8 b:1/8 b:1/8', total_bar_length=1, time_signature=[3,4]) 

#debug statement
#print(rhythm_eights)

def play_zanarkand():

    testing_intro = chord('E6, E5, G5, B5, E6')
    final_testing = testing_intro + D_Fsharp6
    print(final_testing.notes)

    # Defined measures
    m1 = final_testing.apply_rhythm(rhythm_eights) 
   # m2 = chord('E6, G6', duration=3/4)

    song = m1 
    #melody_intro = chord('E6[.8;.],E5[.8;.],G5[.8;.],B5[.8;.],E6[.8;.], D6;F#6[.8;.], E6;G6[3/4;.]')


    play(song, wait=True, save_as_file=False, bpm=86)

