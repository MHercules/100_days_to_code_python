print(r'''
                           ,;;,.                  ,;'',
                    |~|                    |~|
                   ([~])                  ([~])
                 ,_.~~~.                  .~~~.
               ()--|   ,\                /    ,\    ()
            ,_//   |   |>)              (<|   |\()--'m
         (~'  m''~)(   )/                \(   )   ~~'|
          \(~||~)/ ||~||                  ||~||     ||
             ||   ()   ()      PjP       ()   () <( || )>
             ||   ||   ||       -        ||   ||( '-||-' )
             || ,;.)   (.;,            ,;.)   (.;,(~\/~)/
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
''')

print("Welcome Traveler, you have wandered to a Dungeon!!!.")
print("Before you stands two guards, each blocking a cave entrance.")

cave_entrance = input("Will you enter on the left, or right?\n")
if cave_entrance == "right" or cave_entrance == "Right":
    print("The right Guard is in a wrong mood, he swiftly decapitates you!\nGame Over.")
elif cave_entrance == "left" or cave_entrance == "Left":
    gone_left = input("You've arrived at an eerie shadowy lake, will you try to swim across, or wait?(swim/wait)\n")
    if gone_left == "swim" or gone_left == "Swim":
        print("The lake likes you, it craves you, your skin falls off your bone as the lake slowly consumes you.\nGame Over.")
    elif gone_left == "wait" or gone_left == "Wait":
        print("\nYou wait, and wait, and wait... As you're about to give up and swim across, a boat stops in front of you.")
        print("You hesitantly step inside, the boat seemed alive, and in a bad mood. It swayingly and swervingly ferries you across the lake.")
        print("\nFinally and mercifully, you reach the other side. It seemed like days you've been here, months even."
              " But all adventures eventually come to an end.\nYou have a feeling that this might be the end, or yours.\n")
        final_choice = input("Before you lies three paths, the left, the middle and the right. Choose:(left/middle/right)\n")
        if final_choice == "left" or final_choice == "Left":
            print("\nYou step into the path on the left. The world changes around you, cave walls turn to fire, the floor turns to magma."
                  "\nThe devil looks down at you, and grins a toothy, evil, grin...\nGame Over.")
        elif final_choice == "middle" or final_choice == "Middle":
            print("You go straight. The cave walls stretch on endlessly, but still you walk, and walk, and walk..."
                  "\nYour path is blocked by a door. You catch your breath, reach out and slowly open it."
                  "\nYou see gold coins, as high as mountains. Rubies the color of wine. And silver enough to last a few lifetimes."
                  "\nCongratulations, you've won!")
        elif final_choice == "right" or final_choice == "Right":
            print("You go right, and the floor beneath you vanishes."
                  "\nYou fall, forever, and ever, and ever."
                  "\nGame Over.")

