Title:************* Snake Game****************************

**Description:

This Snake Game is a classic implementation of the popular Snake game that we play in mobile phones. This game is entirely created using basic python concepts such as OOP's, datatypes, control flows and very useful modules such as the turtle module, random module and the time module. The objective of the game is to control a snake that grows in length as it consumes food items while avoiding collisions with walls and its own tail. 



**Gameplay:
 
This game is built with a perfect user interface where you can control the movement of the snake using your keybord keys: a: turn left, d: turn right, s: move down, w: move up.  

**Objective:

The objective of this game is to control a snake that grows in length as it consumes food items while avoiding collisions with walls and its own tail. Every time the snake consumes the food item it grows in length and your score increases by 1. The objective is to attain the max score that you can possibly get or to beat your previous high score!.


**Scoring: 

The code has a way to keep track of your previous high score using the open file command in the score.py file. This functionality was included keeping in mind that you never want to settle down with your own high scores! So you can keep playing to beat your high scores and the game will keep track of it for you.


**Customization:

You can modify the speed of the snake by changing the argument in the time.sleep() method found in the main.py file. The default speed is 0.1 you can slowly change this by 0.01...caution: decreasing this value abruptly will make the snake too fast to handle!. If you want to change the keyboard controls you can do this by changing the key argument to your preffered one in the screen.onkeypress() method found in the main.py file: screen.onkeypress(key = "your_keyboard_input").
It is also possible to change the kind of food that randomly pops up on the screen. For this you may need to play around with the food.py file. Try making changes to the food using the .shape() method from the turtle module in the refresh() method found in the food class.

**Challenges: 
This game is the best to sharpen your reflexes. if you really want to push the limits slowly increase the speed of the snake and try beating your high scores!.


**Python game: 

This game is entirely built on python. It showcases a classical game development capabilities of the python libraries such as the turtle module. This project is a perfect example of showcasing basic python coding skills to built an amazing game for fun or for educational purpose!


