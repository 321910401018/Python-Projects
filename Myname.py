#CODE

import turtle as t

t.shape('arrow')
t.pensize(3)


t.speed(5)

t.penup()                       #BACK GAP
t.backward(400)
#-----------------------------------------------------------------------------------
#Draw C
t.pendown()
t.backward(50)
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.penup()
#----------------------------------------------------------------------------------
t.forward(100)                   #GAP
t.left(270)
t.backward(50)
#-----------------------------------------------------------------------------------
#Draw H
t.pendown()
t.left(90)
t.backward(100)
t.forward(50)
t.right(90)
t.backward(50)
t.left(90)
t.forward(50)
t.backward(100)
t.penup()
#--------------------------------------------------------------------------------------
t.forward(100)                   #GAP
t.left(90)
t.forward(50)
#---------------------------------------------------------------------------------------
#draw A
t.pendown()
t.right(90)
t.backward(100)
t.left(90)
t.forward(50)
t.right(90)
t.forward(100)
t.backward(50)
t.left(90)
t.backward(50)
t.penup()
#---------------------------------------------------------------------------------------
t.right(90)                      #GAP
t.forward(50)
t.left(90)
t.forward(100)
#----------------------------------------------------------------------------------------
#Draw R
t.pendown()
t.left(90)
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.left(135)
t.forward(70)
t.penup()
#------------------------------------------------------------------------------------
t.left(45)                        #GAP
t.forward(50)
#------------------------------------------------------------------------------------
#draw A
t.pendown()
t.right(90)
t.backward(100)
t.left(90)
t.forward(50)
t.right(90)
t.forward(100)
t.backward(50)
t.left(90)
t.backward(50)
t.penup()
#--------------------------------------------------------------------------------------
t.right(90)                       #GAP
t.forward(50)
t.left(90)
t.forward(100)
#-----------------------------------------------------------------------------------
#draw N
t.pendown()
t.left(90)
t.forward(100)
t.right(150)
t.forward(111)
t.left(150)
t.forward(100)
#----------------------------------------------------------------------------------------
t.penup()                         #GAP
t.right(180)
t.forward(100)
t.left(90)
t.forward(125)
t.pendown()
#------------------------------------------------------------------------------------
col='red'                         # HEART SHAPE

t.fillcolor(col)

t.begin_fill()

t.right(180)
t.right(135)
t.forward(100)
t.circle(50,180)
t.right(90)
t.circle(50,180)
t.forward(100)

t.end_fill()
#--------------------------------------------------------------------------------------

t.speed(1)
t.penup()
t.forward(1000)
