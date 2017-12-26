

import turtle
def main():

  imageDecision = input("What image would you like to draw? A house or a flower?")
  
  if(imageDecision == "house"):
    houseColor = input("What color would you like your house? red or brown?")
  elif(imageDecision == "flower"):
    flowerColor = input("what color would you like your flower? pink or blue?")
  
  if(imageDecision == "house" and houseColor == "red"):
    redTurtle = turtle.Turtle()
    redTurtle.color("red")
    redTurtle.hideturtle()
    redTurtle.penup()
    redTurtle.setpos(-50,-50)
    redTurtle.pendown()
    redTurtle.forward(100)
    redTurtle.left(90)
    redTurtle.forward(100)
    redTurtle.left(30)
    redTurtle.forward(100)
    redTurtle.left(120)
    redTurtle.forward(100)
    redTurtle.left(30)
    redTurtle.forward(100)
  elif(imageDecision == "house" and houseColor == "brown"):
    brownTurtle = turtle.Turtle
    
    
  
    
  
  
main()
