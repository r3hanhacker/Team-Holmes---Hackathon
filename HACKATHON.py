def abdullahhappy(happy):
  print('<------------------------------------------------------>')
  var_abdullahhappy = input("You walk over to Abdullah, and he's looking pale on the verge of tears.Do you want to: A. Empathise with Abdullah, B. Tell Abdullah you're sorry for not helping him, C. Ask him to get over it and fight, and that he has a team behind him. You tell him that Leonard doesn't define who he is. Choose A, B or C : ")
  if var_abdullahhappy == "A":
    print('<------------------------------------------------------>')
    print("Abdullah bursts into tears and shouts at you to go away. You lose the first game.")
    var_lostmatches = var_lostmatches + 1
  elif var_abdullahhappy == "B":
    print('<------------------------------------------------------>')
    print("Abdullah bursts into tears and shouts at you to go away. You lose the first game.")
    var_lostmatches = var_lostmatches + 1
  elif var_abdullahhappy == "C":
    print('<------------------------------------------------------>')
    print("Well done! Abdullah feels better. You've won the first game!")
  else:
    print("Invalid input")
    exit()    
    
def abdullahbully():
  var_lostmatches = 0
  var_abdullahbully = input("What do you want to do?  A. Smack Leonard and dismiss him,B. Defend Abdullah, or C. Just Watch? Respond with A, B or C : ")
  if var_abdullahbully == "A":
    print('<------------------------------------------------------>')
    print("Leonard isn't one to back down. The two of you get into a fight, and both come out bruised. You're unfit for the first game, and your team loses the first match. Lose two and you're disqualified.")
    var_lostmatches = var_lostmatches + 1
  elif var_abdullahbully == "B":
    print('<------------------------------------------------------>')
    print("You: Calm down Leonard. That was an extremely rude comment, you know how Abdullah is. Please apologise, you hurt his feelings")
    print('<->')
    print("Leonard:Yeah? Think I care? You're all just...UGH leave it")
    print("Although Leonard's still in a bad mood, it just makes his playstyle more agressive, leading you to a successful win!")
  elif var_abdullahbully == "C":
    print('<------------------------------------------------------>')
    print("Nobody has the courage to face down Leonard, and Abdullah is depressed and isn't fit enough for your first game. If you don't get him back into his regular mood, you'll lose for sure! ")
    abdullahhappy()
  else:
    print("Invalid input")
    exit()


def kirabully():
  print('<------------------------------------------------------>')
  var_kirabully = input("What do you want to do? A. Shout at the officer, B. Back down and let Kira fight by herself, C.Leave it be and walk away ")
  if var_kirabully == "A":
    print('<------------------------------------------------------>')
    print("You shout at the officer, 'Why should it be specifically her? She can't control her skin complextion, its biological luck that you have a lighter complextion because of your parents! If you ever touch her again you'll have the entire Team Holmes to answer to, and it won't be pretty.' The officer looks at you wide-eyed and mumbles apologies as he backs away. Kira thanks you and her morale is boosted. You win the second match, and the next. The team morale is high because you protected them from the dangers of racial discrimination.")
    print("<------------------------------------->")
    print("Although awareness is increasing, we must fight hard to protect the Kiras and Abdullahs of the world, and we of Team Holmes ask you to use your logic, and defend those who can't defend themselves. Thank you for playing our game. - Tarafdar and Vittal 26-2-2022")
  elif var_kirabully == "B":
    print('<------------------------------------------------------>')
    print("Kira and the officer fight and Kira is detained for a week. You lose the second match and are completely disqualified")
    var_lostmatches = var_lostmatches + 1
    print("DISQUALIFIED")
    exit()
  elif var_kirabully == "C":
    print('<------------------------------------------------------>')
    print("Kira and the officer fight and Kira is detained for a week. You lose the second match and are completely disqualified")
    var_lostmatches = var_lostmatches + 1
    print("DISQUALIFIED")
    exit()
  else:
    print("Invalid input")
    exit()
    

print("Hey! You've been selected to be the captain of an E-sports team. Being captain is hard, and you need to make the right decisions to win. Oh! we're late, time to meet your team")
print('<------------------------------------------------------>')
print("Leonard; Heir of a rich business empire, agressive, American")
print("Abdullah: Muslim by religion, calm but sensitive, Irani, doesn't accept help easily")
print("Kira: African-American, defensive, an activist at heart")
print('<------------------------------------------------------>')
print("The team lounges in the common room, playing a racing game. Abdullah drops a kart bomb on Leonard")
print("Leonard: Wow Abdullah! You're picking up your entire culture's favorite activity!")
print("Abdullah: What do you mean?")
print("Leonard: Oh, you know, you're all scummy terrorists")
abdullahbully()
print('<------------------------------------------------------>')
print('The team is relaxing on a bench by the docks, trying to figure out a strategy for the championships')
print('A police officer sees them talking on the bench. He sees Kira, and decides to walk over.')
print("You all shouldn't be sitting here, 'specially her...")
print("Kira gets up, with flames burning in her eyes")
print("Kira: And why is it 'especially' me?")
print("Officer: Yo're a black, this is a respectable place for whites and even though the rules aren't written down it's best you get out of here while you can.")
kirabully()
