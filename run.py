# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('fatal_labyrinth')

characters = SHEET.worksheet('characters')
data = characters.get_all_values()


# CHARACTER BUILDING
# Forms player and story character details and stats used in game mechanics
class Character:
    def __init__(self, name, home, health, attack, defense, weapon,
                 clothes, item1, item2):
        self.name = name
        self.home = home
        self.health = health
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.clothes = clothes
        self.item1 = item1
        self.item2 = item2


# All stats are taken from connected GoogleSheet for easy manipulation
player = Character(data[1][1], data[1][2], data[1][3], data[1][4], data[1][5],
                   data[1][6], data[1][7], data[1][8], data[1][9])

helpfulOrb = Character(data[2][1], data[2][2], data[2][3], data[2][4],
                       data[2][5], data[2][6], data[2][7], data[2][8], 
                       data[2][9])

mopeyGoblin = Character(data[3][1], data[3][2], data[3][3], data[3][4],
                        data[3][5], data[3][6], data[3][7], data[3][8], 
                        data[3][9])

nakedWizard = Character(data[4][1], data[4][2], data[4][3], data[4][4],
                        data[4][5], data[4][6], data[4][7], data[4][8], 
                        data[4][9])

hummusDemon = Character(data[5][1], data[5][2], data[5][3],
                        data[5][4], data[5][5], data[5][6], data[5][7],
                        data[5][8], data[5][9])

securityGuardLarry = Character(data[6][1], data[6][2], data[6][3],
                               data[6][4], data[6][5], data[6][6], data[6][7], 
                               data[6][8], data[6][9])


# MECHANICAL FUNCTIONS

def inventory(Character):
    print(f'\nYou are armed with a {Character.weapon}, wearing ' +
          f'{Character.clothes} and carrying a {Character.item1}.' +
          f'There is a {Character.item2} in your pocket.\n')


def rune(Character):
    player.attack = ((int(Character.attack)) * 2)


def exchangeWeapons(player, mopey_goblin):
    player.attack = 80
    player.weapon = "bloodied axe"
    mopeyGoblin.attack = 25
    mopeyGoblin.weapon = "shiny sword"


def noClothes(player):
    player.clothes = "nothing"
    player.defense = 0


# NARRATIVE FUNCTIONS


def introFunc():
    while True:
        print("Do you remember your name? (yes/no)")
        print('Enter "I" at anytime to check your inventory.')
        memoryOfName = input("> ")
        if memoryOfName.lower() in ["yes", "y"]:
            print("\n         :Helpful Orb:")
            print("Good start.")
            print("...so, what is your name?")
            player.name = input("> ")
            if player.name.lower() in ["bob", "robert"]:
                print("\n         :Helpful Orb:")
                print("You look like a Bob!")
                print("We are going to get on great Bob.")
                print("I love that name. Bob, Bob, Bob. I could say it all day.")
            print(f'Well {player.name}, where are you from?')
            player.home = input(">")
            break
        elif memoryOfName.lower() in ["no", "n"]:
            print("\n         :Helpful Orb:")
            print(f"Okay, no stress. It's ummmm... {player.name}! Your name " +
                  f"is {player.name}. Yes.")
            print(f"And in case you're wondering you are from...{player.home}")
            break
        elif memoryOfName.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("\n         :Helpful Orb:")
            print("This is no time for weird answers. Just say yes or no.")


def deathMemoryFunc():
    while True:
        print("Do you remember what happened a moment ago? (yes/no) ")
        playerRemembers = input("> ")
        if playerRemembers.lower() in ["yes", "y"]:
            print("\n         :Helpful Orb:")
            print("You probably already died at least once then.")
            print("The Labyrinth seems to respawn you at this moment in time.")
            print("Oh well, at least I don't need to go over anything.")
            print("Lets try not to do whatever it was we did before. " + 
                  "Onward!\n")
            break
        elif playerRemembers.lower() in ["no", "n"]:
            print("\n         :Helpful Orb:")
            print("I thought you mightn't. I'm The Orb of Helping.") 
            print("You brought me to this danger filled labyrinth,")
            print("to help you find an ancient relic.")
            print("We set off a booby-trap,")
            print("which appears to have given you mild magical amnesia.")
            print("We are lost, currently escaping, and now you're all " +
                  "caught up.")
            print("Let's go!\n")
            break
        elif playerRemembers.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("\n         :Helpful Orb:")
            print("Oh he's gone mad... I was worried this would happen.")
            print("I'll speak slower.")


def firstChoiceFunc():
    while True:
        print("\nDo you choose to go left or right? (L/R) ")
        forkOne = input("> ")
        if forkOne.lower() in ["left", "l"]:
            print("     -You proceed into the Labyrinth")
            print("You chat to the orb in your hand as you pad down the hall.")
            print("It's nice to meet someone with similar interests.")
            print("There is a rushing sound of wind ahead.")
            print("You turn a corner to find an Air Elemental facing you.")
            print("The being of pure wind gusts towards you.")
            print("You have no defense for this!")
            print("The orb is knocked from your hand, you hear a smash" + 
                  " and the hall goes dark")
            print("You are pressed against the wall as the air is forced " +
                  "from your lungs.")
            print("You gasp for your last breath in the darkness of the " +
                  "labyrinth")
            print("YOU ARE DEAD - TRY AGAIN")
            print(f'{player.name} of {player.home} is no more.')
            exit()
        elif forkOne.lower() in ["right", "r"]:
            print("\nAs you cross the threshold of the right tunnel")
            print("you feel invigorated, the rune on the wall glows briefly.")
            rune(player)
            break
        elif memoryOfName.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("We need to pick a tunnel, not stand here nattering.")


def goblinEncounterFunc():
    while True:
        print("Would you like to:")
        print("1- Ask if he is okay?")
        print("2- Sneak attack with your sword")
        print("3- Take off your clothes and run at him")
        print('Enter the number of your choice:')
        mopeyGoblinEncounter = input("> ")
        if mopeyGoblinEncounter.lower() in ["1", "one"]:
            print(f"\n           :{player.name}:")
            print('"Are you alright friend?"')
            print("\n         :Mopey Goblin:")
            print("Other Gobbos soaked my axe in pigs blood, it's ruined.")
            print("Just having a rubbish day, I'm alright.")
            print("Thanks for asking. Do you need something?")
            goblinsQuestionFunc()
            break
        elif mopeyGoblinEncounter.lower() in ["2", "two"]:
            print("\nYou draw your sword and creep towards the creature.")
            print("As you approach, the Helpful Orb gasps, realising your intention")
            print("The Goblin looks up at the sound and snarls at you.")
            print("He is lightning fast, the axes flashes sideways")
            print("You parry but it knocks you against the wall.")
            print("He raises the axe above his head and brings it down on your sword arm.")
            print("The limb drops to the floor and you go dizzy.")
            print("The Goblin stands back to admire his handy work.")
            print("Then lazily swings the axe at you throat.\n")
            print("         :Mopey Goblin:")
            print('Youve cheered me right up\n')
            print("YOU ARE DEAD - TRY AGAIN")
            print(f'{player.name} of {player.home} is no more.')
            exit()
        elif mopeyGoblinEncounter.lower() in ["3", "three"]:
            print("\nYou decide upon shock and awe.")
            print('"Bold!" you think as you strip down in the dark tunnel.')
            print('"Come out swinging" you say to yourself.')
            print("The Goblin was not expecting a nude being here.")
            print("Your flailing arms and screaming is disconcerting.")
            print("However the hallway is long and his reflexes are honed.")
            print("He hurls the axe at your unarmoured chest.")
            print("You catch the axe dead center mass.")
            print("This is a quick death.")
            print("What were you expecting would happen?")
            print("\nYOU ARE DEAD - TRY AGAIN")
            print(f'{player.name} of {player.home} is no more.')
            exit()
        elif mopeyGoblinEncounter.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("\nOnly death lies behind")
            print("You must choose.")


def goblinsQuestionFunc():
    while True:
        print('1- "Just looking for the way out mate?"')
        print('2- "No, I am taking my orb for a walk. Hope your stuff all' +
              ' works out."')
        print('3- "I will trade you this clean sword for that dirty axe if' +
              ' you like?"')
        print('Enter the number of your choice')
        mopeyGoblinQuestion = input("> ")
        if mopeyGoblinQuestion.lower() in ["1", "one"]:
            print("Oh just go back the way I came, take the second left " +
                  "after the screaming bulls head on the wall and head " +
                  "straight. Can't miss it\n")
            print("You hurry off down the corridor.")
            print("As you pass a screaming bulls head. Cackles sound nearby")
            print("The echoes make it impossible to find the source")
            print("You sprint down the second corridor to the left")
            print("Running headlong into a gang of vicous happy Goblins")
            print("Before you can ask how they are feeling," +
                  " a blow dart impacts your neck.")
            print("You feel the poison burning. You have seconds to live.")
            goblinDeathChoice()
        elif mopeyGoblinQuestion.lower() in ["2", "two"]:
            print("          :Mopey Goblin:")
            print("Lovely looking orb. Have a nice walk.\n")
            print("He begins to mop blood off the axe and ignores you.")
            print("As you stroll passed him you hear a flurry of motion")
            print("The axe bites into your back.")
            print("You fall to the floor. Your body goes numb.")
            print("This isn't how it was meant to end.")
            print("The orb falls to the floor and the Mopey Goblin " +
                  "picks it up.")
            print("He gives you a grin...and swings the axe up above" +
                  " his head.")
            print("YOU ARE DEAD - TRY AGAIN")
            print(f'{player.name} of {player.home} is no more.')
            exit()
        elif mopeyGoblinQuestion.lower() in ["3", "three"]:
            print("hurray")
        else:
            print("The Mopey Goblin stares at you intently, waiting.")


def goblinDeathChoice():
    while True:
        print("1- drink the potion in your pocket")
        print("2- throw the Orb of Helping at the goblin gang")
        print('Enter the number of your choice')
        goblinDeathChoice = input("> ")
        if goblinDeathChoice.lower() in ["1", "one"]:
            print("Your hands tingle, they swell and begin to grow.")
            print("You die with massive hands and goblins laughing" +
                  " hysterically around you as your face goes purple.")
            print("YOU ARE DEAD - TRY AGAIN")
            print(f'{player.name} of {player.home} is no more.')
            exit()
        elif goblinDeathChoice.lower() in ["2", "two"]:
            print("You hurl the screaming orb at the largest goblin")
            print("Your only friend and source of light smashes and curses" +
                  " your name")
            print("You die in darkness as goblins cackle and crowd in")
            print("YOU ARE DEAD - TRY AGAIN")
            print(f'{player.name} of {player.home} is no more.')
            exit()
        else:
            print(f'You shout "{goblinDeathChoice}", which means nothing to' +
                  ' anyone but you.')
            print("The poison dart works quickly")
            print("You die in the tunnels. The Helpful Orb weeps for you.")
            print("YOU ARE DEAD - TRY AGAIN")
            print(f'{player.name} of {player.home} is no more.')
            exit()


# GAME START

# Chapter 1 - Intro 
print("YOU ARE IN THE FATAL LABYRINTH\n")
print("You wake to find yourself in a dark stone corridor, the floor is sand.")
print("The air is musty, in your hand a glowing sphere throbs gently.")
print("The Orb pulses and a voice emanates from inside.\n")
print("         :Helpful Orb:")
print("Hello again")

introFunc()

print(f'Well {player.name} this whole situation may seem a little \
disconcerting at first.')

deathMemoryFunc()

print("     -You proceed into the labyrinth-")
print("There is a fork in the tunnel ahead.")
print("The right path has a rune on the wall.")
print("The left path has fresher smelling air.")

firstChoiceFunc()

# Chapter 2A - Right Fork - Mopey Goblin Encounter

print("You travel down the gloomey tunnels")
print("Light comes only from the Helpful Orb")
print("You round a corner to find a bench up ahead hewn into the rock wall")
print("Sat on the bench is a goblin, his head is downcast, he looks sad.")
print("He hasn't noticed you yet") 
print("A wicked looking axe in his hand is drenched in blood, it drips.\n")

goblinEncounterFunc()

print("     -You proceed into the labyrinth-")

        
"""
        1a Just looking for the way out? - Mopey_Goblin gives bad advice
        2a No, I'm taking my orb for a walk. Hope your stuff all works out. - Mopey_Goblin goes back to moping
        3a I'll trade you this clean sword for that manky axe if you like? - Mopey_Goblin accepts trade
            Mopey_Goblin: 1a Oh just go back the way I came, take the second left after the screaming bulls head on 
                             the wall and head straight. Can't miss it
                          2a "Lovely looking orb. Have a nice walk." Begins to mop blood off the axe and ignores you.
                          3a That would be really great. Here you go, it's a brilliant axe once you've cleaned it. 
                            Thank you. I wouldn't hang about, the others arent keen on humans. You seem like one of
                            the good ones though
                              
                                - 

"""