import turtle

t = turtle.Turtle()
myWin = turtle.Screen()

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

turtle.done()
myWin.exitonclick()
