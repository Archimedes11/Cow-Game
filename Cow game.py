#Adam K. Wolff
#Created on 03/30/14, Updated 11/05/2020
#adam@adamkwolff.com


'''
  Purpose: To create a game in which a user can select if they want
    to play and clicks in the window to try to find the hidden cow, accompanied
    by a "hot or cold" box to clue the user in to how close or far they may be
    from the location of the cow - which changes each round played.
  
  Preconditions: Window opens and user clicks as to whether or not they want to
    play, and when the game begins, they click in the window until they find the
    location of the hidden cow.  User can then select to play again or not.
    
  Postconditions: Game either ends with a message and a click or begins based
    on the user's decision.  During the game, the program waits for user clicks, 
    the locations of which determine the color of the "hot or cold" box, with
    warmed colors the closer the user gets to the hidden cow.  When a click falls
    within a certain distance of the denter of the cow, the gif will appear and
    how many times the user clicked will be displayed along with whether or not
    it was a new low score.  Game executes another time if user selects to play
    again.
'''
#import graphics math and random
from graphics import *
from math import *
from random import *

#yes_or_no
'''
 preconditions = window
 
 purpose: User clicks to play the game which initiates the rest of the program,
   or chooses not to by clicking anywhere else and closing the window.
   
 postconditions = If the user's click is within the dimensions of the 'yes' box,
   the function will return a value to begin the game.  Otherwise, a message
   will be displayed and a click will close the window.
'''
def yes_or_no(win):
    
    #Draws a yes box
    yesBox = Rectangle(Point(5,5), Point(80,80))
    yesBox.draw(win)
    
    #draws a yes inside the box
    yesboxTitle = Text(Point(37.5,37.5), "YES")
    yesboxTitle.setStyle('bold')
    yesboxTitle.draw(win)
    
    #Asks the user is they want to play
    playAgain = Text(Point(120,120), "You want to play??")
    playAgain.setStyle('bold')
    playAgain.draw(win)    
    
    #Gets a click from the user, determines the coordinates and then determines
    # whether or not it was inside the yes box.
    click=win.getMouse()
    clickX=click.getX()
    clickY=click.getY()    
    
    if clickX > 5 and clickX < 80 and clickY > 5 and clickY < 80:
        playGame = True
    else:
        playGame = False
    
    #undraws everything.                                          
    yesBox.undraw()
    yesboxTitle.undraw()
    playAgain.undraw()
    
    #returns the playGame flag.
    return playGame



#find_distance
'''
 preconditions = program waits for the location of a user click
 
 purpose: The location of each click will be compared to the location of the cow
   and the distance will determine the color shown in the "hot or cold" box.
   When the distance is so close that the user has hit the cow, the loop will end.
   
 postconditions = function returns how many clicks it took to hit the cow
'''
def find_distance(win,cowX,cowY):
    
    #Gets a mousclick and determines the coordinates of the click.
    click=win.getMouse()
    clickX=click.getX()
    clickY=click.getY()
    
    #Gets a distance between the cow and the click.
    distance =sqrt(((cowX-clickX)**2)+((cowY-clickY)**2))
    
    #Returns the distance.
    return distance



#hot_or_cold
'''
 preconditions = function gets distance as its arguements
 
 purpose: The function will determine which color to color the box.
   
 postconditions = Function will return the color for which distance is recieves.
'''
def hot_or_cold(distance):
    
    #Determine which color to return
    if distance <= 150:
        color="red"
    if distance > 150 and distance <= 250:
        color="pink"
    if distance > 250 and distance <= 350:
        color="lightblue"
    if distance > 350:
        color="blue"
    
    #Return the correct color.
    return color

def main():
    
    #Creates graphics window
    win = GraphWin("The Cow Game", 500, 500)
    
    #calls yes_or_no function
    playGame=yes_or_no(win)
    
    #if they click no close the program.
    if playGame == False:
        endingTitle2 = Text(Point(200,420), "Goodbye! Click to close.")
        endingTitle2.setStyle('bold')
        endingTitle2.draw(win)
        win.getMouse()
        win.close()    
    
    #Set some variable to their starting values.
    color="blue"
    numClick=0
    numClickstr="0"
    numClickTitle2 = Text(Point(115,485),"")
    bestScore=9999*9999

    #While the user wants to play:
    while playGame == True:
        
        #Get coordinates for the cow pic.
        cowX=randrange(75,425)
        cowY=randrange(75,425)
        
        #shows hot or cold text.
        hotorcoldTitle = Text(Point(350,490), "Hot or Cold")
        hotorcoldTitle.setStyle('bold')
        hotorcoldTitle.draw(win)
        
        #draws the color box       
        hotorcoldbox = Rectangle(Point(340,420),Point(360,470))
        hotorcoldbox.setFill(color)
        hotorcoldbox.draw(win)        
        
        #calls the distance function and assignes the valie to the variable distance.
        distance = find_distance(win,cowX,cowY)
        
        #undraws the hot or cold box and title
        hotorcoldTitle.undraw()
        hotorcoldbox.undraw()
        
        #While the user hasn't clicked the cow:
        while distance > 55:
            
            #draws hot or cold text
            hotorcoldTitle = Text(Point(350,490), "Hot or Cold")
            hotorcoldTitle.setStyle('bold')
            hotorcoldTitle.draw(win)
            
            #Gets a color form the hot_or_cold function
            color = hot_or_cold(distance)
            
            #adds one to the accumulator numClick and turns it into a str as well.        
            numClick+=1
            numClickstr=str(numClick)           
            
            #draws the color box
            hotorcoldbox = Rectangle(Point(340,420),Point(360,470))
            hotorcoldbox.setFill(color)
            hotorcoldbox.draw(win)
            
            #draws the clicks: text
            numClickTitle = Text(Point(75,485), "Clicks: ")
            numClickTitle.setStyle('bold')
            numClickTitle.draw(win)
            
            #undraw the previos click
            numClickTitle2.undraw()
            
            #draw the new click.
            numClickTitle2 = Text(Point(115,485),numClickstr)
            numClickTitle2.setStyle('bold')
            numClickTitle2.draw(win)
            
            #gets a click and distance from the find_distance function
            distance = find_distance(win,cowX,cowY)
            
            #undraws everything
            hotorcoldTitle.undraw()
            hotorcoldbox.undraw()
            numClickTitle.undraw()
            numClickTitle2.undraw()            
        
        #if number of clicks is less than the best score lowest = true and
        #best score is equal to the nubmer of clicks.
        if numClick < bestScore:
            lowest = True
            bestScore=numClick
        else:
            lowest = False
        
        #if it is the lowest amount of clicks output A new lowest!!!
        if lowest == True:
            congratsTitle = Text(Point(200,380), "A new lowest!!!")
            congratsTitle.setStyle('bold')
            congratsTitle.draw(win)            
        
        
        #output you found it!!  
        congratsTitle2 = Text(Point(200,420), "You Found It!")
        congratsTitle2.setStyle('bold')
        congratsTitle2.draw(win)
        
        #output clicks: 
        numClickTitle3 = Text(Point(200,440), "Clicks: ")
        numClickTitle3.setStyle('bold')
        numClickTitle3.draw(win)
        
        #output the number of clicks   
        numClickTitle4 = Text(Point(240,440),numClickstr)
        numClickTitle4.setStyle('bold')
        numClickTitle4.draw(win)
        
        #draw the cow picture.
        cowpic = Image(Point(cowX,cowY), "cow.gif")
        cowpic.draw(win)
        
        #get a mouse click
        win.getMouse()
        
        #undraw everything
        congratsTitle.undraw()
        congratsTitle2.undraw()
        numClickTitle3.undraw()
        numClickTitle4.undraw()
        cowpic.undraw()

        
        
        #call playGame function
        playGame=yes_or_no(win)
        #set numClick back to zero
        numClick=0
        
        #If playGame is equal to false then say goodbye, get a mouse click, and close the program.
        if playGame == False:
            
            endingTitle2 = Text(Point(200,420), "Goodbye! Click to close.")
            endingTitle2.setStyle('bold')
            endingTitle2.draw(win)
            win.getMouse()
            win.close()
            
main()
        
        
        
        
        
        
        
        
        
    
    
