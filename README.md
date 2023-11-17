# chemMeasure
CS 482 Capstone Project


_Notes:_

- [x] Add selection for number of pixels
  - Can get the number of pixels manually using Paint 3D. Auto-detection is unreliable.
- [ ] Add input for reference bar unit type
- [ ] Add selection for displaying circles (to aid in troubleshooting)
- [ ] Connect scale calculator to form
  - [ ] Remember to replace values in math calculations to the result of the scale calculator
    - [ ] and to min dist, min rad, and max rad
- [ ] add num circles param
- [ ] add circle detector debugging
- [ ] add the diameter of the overlapping section of the circles (DIB diameter)


Possible solution for outlier circles is to have a running average for the size of a given circle and if the result is a
significant outlier, to ignore it.

Possible solution for multiple circles is that if the position of the center has not moved enough, to ignore it
Also could use position to ID different circles.
Also could use position to identify area where more accurate circles are likely to lie
    Cannot. Some videos change position.
