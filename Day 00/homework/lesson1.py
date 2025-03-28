from turtle import *


#make a house


width(7)
color("blue")
begin_fill()
speed(999999)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
end_fill()
#end of square

#the start of the door

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(100, 220)
pendown()

color("cyan")
begin_fill()
right(60)
forward(35)
right(90)
forward(50)
right(90)
forward(70)
right(90)
forward(50)
right(90)
forward(50)
end_fill()






exitonclick()



name = "levani" 
print(name)




