import turtle as t

marker = t.Turtle()


for _ in range(13):
    marker.forward(5)
    marker.penup()
    marker.forward(5)    
    marker.pendown()
    
scree = t.Screen()
scree.exitonclick()