#Author : Abhinav Mahapatra
#Date: 11/1/2017


#Do a pip install turtle if you haven't downloaded turtle module in python libraries
import turtle

#initializing turtle
t = turtle.Turtle()
#initializing the screen
myWin = turtle.Screen()

#defining the tree fractal funtion
def tree(length = 100):

    if length < 1:
        return
    t.forward(length)
    t.left(30)
    tree(length *.7)
    t.right(60)
    tree(length * .7)
    t.left(30)
    t.backward(length)
    return

t.right(-90)
tree()

#closing the turtle screen
turtle.done()
myWin.exitonclick()
