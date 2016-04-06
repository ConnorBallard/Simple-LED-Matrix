# Simple-LED-Matrix

What it does.

Takes the x and y co-ordinate from the skywriter PCB and then converts that into a light patter on an LED matrix
the final version will have sound.

### Things to do / Problems, can't fix

# No.1 Add Python Sonic to the Script
# aim to get a single note working first like a piano
    What i need to happen in simple terms, is for every single x co-ordinate placed to the right the pitch of a note needs to go higher
    for every note it goes left on the x axis needs to drop in pitch

# Expansion
    For every y axis increase/decrease the volume, higher = louder - Lower = Quieter
    For every z axis in both directions change the speed of the note being played.
    Instead of playing a single note, it would need to play arpegios.
      Sonic Pi already has scales in format; 
      Use arpegios as following notes, 
      
      Theme Wonder
      C0-E1-C0-G2-C0-G2-C0-E1
      E1-C0-G2-C0-G2-C0-E1-C0
      etc
      
      theme Harmonic Lead
      G2-E2-C2-E2-G3-E3-C3-E3
      A2-F2-D2-F2-A3-F3-D3-F3
      etc
      
      Minor Triads
      C0-E0-G0-E0-C1-E1-G1-E1
      D0-F0-A0-F0-D1-F1-A1-F1
      etc
      
      3 themes in total - Any more will make a very very long script.
    
    The Z axis needs to control the brightness and speed.
      Everytime a note is played on the arpeggios the light will have need to
      go from lowest to full brightness and back down, Like a blink with sound.
      
      for every lets say 1cm you get closer to the skywriter the refresh rate and speed of that blink increase by 25% but do it so its out of 100%

I would also like the colour to randomly circulate when the object is being used.
