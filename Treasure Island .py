print('''
                     [| .
                      :'m`.
                     ,:mmm:.
                      |,'.|
       ,',           ,':::`.
     ,':::`.   ,'.    u---u
      |,'.|  ,':::`.  |,'.|
     ,':::`.  ||=||  ,':::`.
      u|-|u   |,'.|   u|-|u
      ||,||  ,'mmm`.  ||,||
      ;;u;;u;;|"|"|;;u;;u;;
    , ||:;:;:;|=|=|:;:;:;|| ,
l42_n_||;:;:;:|=|=|;:;:;:||_n____

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
user = input('You came to a park. Where do you want to go? Type "left" or "right" \n').lower()
if user == "left":
  user_1 = input('You came to a pool. What you want to do? Type "swim" or "wait"\n').lower()
  if user_1 == "wait":
    user_2 = input('There is a door. Which door you want to go through? "Red", "Yellow", or "Blue"\n').lower()
    if user_2 == "blue":
      print("Eaten by beasts. Game Over.")
    elif user_2 == "yellow":
      print("You Win!")
    else:
      print("Burned by fire. Game Over.")
  else:
    print(" Attacked by trout. Game Over.")
else:
  print("Fall into a hole. Game Over.")


  
  