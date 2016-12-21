import graphics
from graphics import *


def text(a,b,c,d,e, win):

    write = Text(Point(a,b), c)
    write.draw(win)
    write.setSize(d)
    write.setFill(e)
    write.setFace("courier")
    return write

def rectangle(a,b,c,d,e,win):
    rect = Rectangle(Point(a,b),Point(c, d))
    rect.draw(win)
    rect.setFill(e)
    return rect

def line(a,b,c,d,e,win):
    li = Line(Point(a,b),Point(c,d))
    li.draw(win)
    li.setOutline(e)
    return li

def circle(a,b,c,d,e,win):
    #global circ
    circ = Circle(Point(a,b),c)
    circ.draw(win)
    circ.setOutline(d)
    circ.setFill(e)
    return circ

def entrys(a,b,c,win):
    #global circ
    entr = Entry(Point(a, b),c)
    entr.draw(win)

    return entr
def image(a,b,c,win):
    img = Image(Point(a,b),c)
    img.draw(win)
    return img


               
            






        
