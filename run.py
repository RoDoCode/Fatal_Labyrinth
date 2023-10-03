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
# This forms player and story character details and stats used in game mechanics
class Character:
    def __init__(self, name, home, health, attack, defense, weapon, clothes, item1):
        self.name = name
        self.home = home
        self.health = health
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.clothes = clothes
        self.item1 = item1


# All stats are taken from connected GoogleSheet for easy manipulation
player = Character(data[1][1], data[1][2], data[1][3], data[1][4], data[1][5],
                   data[1][6], data[1][7], data[1][8])

helpfulOrb = Character(data[2][1], data[2][2], data[2][3], data[2][4],
                       data[2][5], data[2][6], data[2][7], data[2][8])

mopeyGoblin = Character(data[3][1], data[3][2], data[3][3], data[3][4],
                        data[3][5], data[3][6], data[3][7], data[3][8])

nakedWizard = Character(data[4][1], data[4][2], data[4][3], data[4][4],
                        data[4][5], data[4][6], data[4][7], data[4][8])

hummusDemon = Character(data[5][1], data[5][2], data[5][3],
                        data[5][4], data[5][5], data[5][6], data[5][7],
                        data[5][8])

securityGuardLarry = Character(data[6][1], data[6][2], data[6][3],
                               data[6][4], data[6][5], data[6][6], data[6][7], 
                               data[6][8])


# MECHANICAL FUNCTIONS

def inventory(Character):
    print(f'\nYou are armed with a {Character.weapon}, wearing ' +
          f'{Character.clothes} and carrying a {Character.item1}.\n')


def rune(Character):
    player.attack = ((int(Character.attack)) * 2)
    print(f'\nYour attack strength has doubled\n')


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
            print(f'Well {player.name}, where are you from?')
            player.home = input(">")
            break
        elif memoryOfName.lower() in ["no", "n"]:
            print("\n         :Helpful Orb:")
            print(f"Okay, no stress. It's ummmm... {player.name}! Your name \
is {player.name}. Yes.")
            print(f"And in case you're wondering you are from...{player.home}")
            break
        elif memoryOfName.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("\n         :Helpful Orb:")
            print("This is no time for weird answers. Just say yes or no.")


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

while True:
    print("Do you remember what happened a moment ago? (yes/no) ")
    playerRemembers = input("> ")
    if playerRemembers.lower() in ["yes", "y"]:
        print("\n         :Helpful Orb:")
        print("You probably already died at least once then.")
        print("The Labyrinth seems to respawn you at this moment in time.")
        print("Oh well, at least I don't need to go over anything.")
        print("Lets try not to do whatever it was we did before. Onward!\n")
        break
    elif playerRemembers.lower() in ["no", "n"]:
        print("\n         :Helpful Orb:")
        print("I thought you mightn't. I'm The Orb of Helping.") 
        print("You brought me to this danger filled labyrinth,")
        print("to help you find an ancient relic.")
        print("We set off a booby-trap,")
        print("which appears to have given you mild magical amnesia.")
        print("We are lost, currently escaping, and now you're all caught up.")
        print("Let's go!\n")
        break
    elif playerRemembers.lower() in ["i", "inventory"]:
        inventory(player)
    else:
        print("\n         :Helpful Orb:")
        print("Oh he's gone mad... I was worried this would happen.")
        print("I'll speak slower.")

print("\n         :YOU PROCEED:")
print("There is a fork in the tunnel ahead.")
print("The right path has a rune on the wall.")
print("The left path has fresher smelling air.")

while True:
    print("\nDo you choose to go left or right? (L/R) ")
    forkOne = input("> ")
    if forkOne.lower() in ["left", "l"]:
        print("UNKNOWN")
        break
    elif forkOne.lower() in ["right", "r"]:
        print("\nAs you cross the threshold of the right tunnel")
        print("you feel invigorated, the rune on the wall glows briefly.")
        rune(player)
        break
    elif memoryOfName.lower() in ["i", "inventory"]:
        inventory(player)
    else:
        print("We need to pick a tunnel, not stand here nattering.")

# Chapter 2A - Right Fork - Mopey Goblin Encounter

print("You travel down the gloomey tunnels")
print("Light comes only from the Helpful Orb")
print("You round a corner to find a bench up ahead hewn into the rock wall")
print("Sat on the bench is a goblin, his head is downcast, crying")
print("He hasn't noticed you yet") 
print("A wicked looking axe in his hand is drenched in blood, it drips.\n")

while True:
    print("Would you like to:")
    print("1- Ask if he is okay?")
    print("2- Sneak attack with your sword")
    print("3- Hurl the Helpful Orb at him")
    print("4- Take off your clothes and run at him")
    print('Enter the number of your choice')
    mopeyGoblinEncounter = input("> ")
    if mopeyGoblinEncounter.str.lower() in ["1", "one"]:
        print("\nYou call to him.")
        print('"Are you alright friend?"')
        print("\n         :Mopey Goblin:")
        print("Other Goblins soaked mi' axe in pigs blood, it's disgusting.")
        print("Just had a rubbish day really, I'm alright.")
        print("Thanks for asking. Do you need something?")
        break
    elif mopeyGoblinEncounter.str.lower() in ["2", "two"]:
        print("\n")
        break
    elif mopeyGoblinEncounter.str.lower() in ["3", "three"]:
        print("\n")
        break
    elif mopeyGoblinEncounter.str.lower() in ["4", "four"]:
        print("\n")
        break
    elif mopeyGoblinEncounter.lower() in ["i", "inventory"]:
        inventory(player)
    else:
        print("\nOnly death lies behind")
        print("You must choose.")
        
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
                              1a - You hurry off down the corridor as you pass the screaming bulls head. You 
                              hear the sound of cackling from somewhere in the tunnels, the echoey accoustics make it 
                              impossible to tell where it's coming from. You feel fear emmanating from the Orb. You 
                              sprint down the second corridor left after the Bull and run headlong into a gang of vicous 
                              and upbeat Goblins. Before you can ask how they are feeling, a blow dart impacts your neck. 
                              You feel the poison burning. You have seconds to live. 
                                - drink potion - your hands tingle, they swell and begin to grow. You die with massive hands and goblins laughing hysterically around you
                                - throw the orb - your only source of light smashes and curses your name, you die in darkness and goblins cackle
                                - 
                                - 

"""