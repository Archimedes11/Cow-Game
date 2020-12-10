from graphics import *

def bird():
    win = GraphWin("Don't Match!!", 500, 500)
    
    cowpic = Image(Point(250,250),"cow.gif")
    cowpic.draw(win) 
    
    yesBox = Rectangle(Point(215,215), Point(285,285))
    yesBox.draw(win) 
    
    win.getMouse()
bird()