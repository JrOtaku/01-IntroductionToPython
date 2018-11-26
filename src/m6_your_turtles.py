"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Emily Guajardo
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# TODO: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

BlueBro = rg.SimpleTurtle('turtle')
BlueBro.pen = rg.Pen('blue',5)
BlueBro.speed = 25
for k in range (80):
    BlueBro.draw_square(100)
    BlueBro.pen_up()
    BlueBro.forward(5)
    BlueBro.right(5)
    BlueBro.pen_down()

GreenBro = rg.SimpleTurtle('turtle')
GreenBro.pen = rg.Pen('green',5)
GreenBro.speed = 25
x = 100
y = 100
for j in range (5):
     GreenBro.draw_circle(150)
     GreenBro.pen_up
     x = x + 20
     y = y + 20
     GreenBro.go_to(rg.Point(x,y))
     GreenBro.pen_down
