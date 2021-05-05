print('''

                                 [O]
                                 [O]
                                 [O]
          ____   /`  ___          ||
      ___/O|__\_/_  /___\         ||
     /_____\__/___/|x===o|        ||
______(o)_______(o)||___||________||________
JRO    ________  ~.>\`    '    ________
 .  '  \__[]__/  '  ^^   .  .  \[]____/ '
       //\__/\\  '    ((())    /_/o\\\
  '.   ( o__o )       aa((((    <_  )/
        \ __ /  .  '  \-(((( .   \__/   .
 .     __\__/___      / /\\(     /   \
      /| \||/  |\    ( ( //  .  ||PD|| '  .
     / |  \/  @| \    \ //      ||  ||
    /  |_  __  |\ \   /[__]   ' ||  ||  .
.   \____|//_| |/ /  /_____\    ||__||
       |       |\/    | | | .   | / \|
       |_______|/     | | |     |_\\\|   .
        |     | .   ' |_|_|      |   |
 .'     |  |  |      <-<--/      |   |
        |  |  |  '  '  .      '  |   |  '  '
  .     |__|__|                  |___|
       (__) (__)      .  '      (____)  
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")

choice1 = input('You\'re at a crossroad, where do you want to go. Type "left" or "right".\n').lower()
if choice1 == "left":
#continue in game
   choice2 = input('You\'ve come to a lake. There is an Island in the middle of the lake. Type "wait" to wait for a boat. Type "swim to swim accros.\n').lower()
   if choice2 == "wait":
       #game will continue
       choice3 = input("You arived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.\n Which color do you choose\n").lower()
       if choice3 == "red":
            print("Its a room full of fire. Game over.")
       elif choice3 == "yellow":
            print("You found the treasure! You win!")
       elif choice3 == "blue":
            print("You enter a room of lions. Game over!")
       else:
            print("You choosed a door that does not exist")
            pass
   else:
        print ("You got attacked by an angry trout. Game over")
else:
    print("Oh oh!") 
    print("You fell into a hole. Game over!")