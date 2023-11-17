# chemMeasure
CS 482 Capstone Project


_Notes:_

- [ ] Add selection for number of pixels and reference bar size
  - Can get the number of pixels manually using Paint 3D. Auto-detection is unreliable.
- [ ] Add input for reference bar unit type


Possible solution for outlier circles is to have a running average for the size of a given circle and if the result is a
significant outlier, to ignore it.

Possible solution for multiple circles is that if the position of the center has not moved enough, to ignore it

Also could use position to ID different circles.

Also could use position to identify area where more accurate circles are likely to lie
