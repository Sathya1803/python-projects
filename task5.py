print('''
******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')
print("welcome to treasure island!")
print("your mission is to find the treasure")
choice1=input('your at the crossroad type "left" or "right" to turn\n')
if(choice1=='left'):
    choice2= input('there is a lake in the island, you want to wait for the boat type "wait" or you want to swim type"swim" \n')
    if(choice2=='wait'):
        choice3=input('there is 3 doors in the room which color door you want type"red","yellow","blue" \n')   
        if(choice3=='red'):
            print("room burned by fire.Game Over. ")
       
        elif(choice3=='yellow'):
            print("you found the treasure.You Win.")
       
        elif(choice3=='blue'):
            print("room full of beasts.Game over")
        
        else:
            print("you choosen the door that is not existed.Game Over.")
    else:
        print("you are attacked by angry trout.Game over")        
         
     
else:
    print("you fell into the hole game over")                      
    


