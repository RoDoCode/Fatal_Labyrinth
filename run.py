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
# This forms character details and stats used in game mechanics
class Character:
    def __init__(self, name, home, health, attack, defense):
        self.name = name
        self.home = home
        self.health = health
        self.attack = attack
        self.defense = defense


player = Character(data[1][1], data[1][2], data[1][3], data[1][4], data[1][5])
mopey_goblin = Character(data[2][1], data[2][2], data[2][3], data[2][4], 
                         data[2][5])
naked_wizard = Character(data[3][1], data[3][2], data[3][3], data[3][4], 
                         data[3][5])
hummus_demon = Character(data[4][1], data[4][2], data[4][3], data[4][4], 
                         data[4][5])
security_guard_larry = Character(data[5][1], data[5][2], data[5][3], 
                                 data[5][4], data[5][5])

# FUNCTIONS

def rune():
    print player.attack
    player.attack = (player.attack * 2)
    print(f'Your attack strength has double')
    print(player.attack)

# GAME START

print("You wake to find yourself in a dark stone corridor, the floor is sand.")
print("The air is musty, in your hand a glowing sphere throbs gently.")
print("The Orb pulses and a voice emanates from inside.")
while True:
    print("Helpful Orb: Hello again, do you remember your name? (yes/no) ")
    memoryOfName = input("> ")
    if memoryOfName.lower() in ["yes", "y"]:
        print("Good start.")
        print("...so, what is your name?")
        player.name = input("> ")
        print(f'Well {player.name}, where are you from?')
        player.home = input(">")
        break
    elif memoryOfName.lower() in ["no", "n"]:
        print(f"Okay, no stress. It's ummmm... {player.name}! Your name is \
{player.name}. Yes.")
        print(f'And in case you were wondering you are from...{player.home}')
        break
    else:
        print("This is no time for weird answers. Just say yes or no.")

print(f'Well {player.name} this whole situation may seem a little \
disconcerting at first.')

while True:
    print("Do you remember what happened a moment ago? (yes/no) ")
    playerRemembers = input("> ")
    if playerRemembers.lower() in ["yes", "y"]:
        print("You probably already died at least once then.")
        print("Oh well I don't need to go over anything.")
        print("Lets try not to do whatever it was we did before. Onward!")
        break
    elif playerRemembers.lower() in ["no", "n"]:
        print("I thought you mightn't. I'm The Orb of Helping.") 
        print("You brought me to this danger filled labyrinth,")
        print("to help you find an ancient relic.")
        print("We set off a booby-trap,")
        print("which appears to have given you mild magical amnesia.")
        print("We are lost, currently escaping, and now you're all caught up.")
        print("Let's go!")
        break
    else:
        print("Oh he's gone mad... I was worried this would happen.")
        print("I'll speak slower.")

print("There is a fork in the tunnel ahead.")
print("The right path has a rune on the wall, from the left the air smells fresher")

while True:
    print("Do you go left or right? (L/R) ")
    forkOne = input("> ")
    if forkOne.lower() in ["left", "l"]:
        print("UNKNOWN")
        break
    elif forkOne.lower() in ["right", "r"]:
        print("As you cross the threshold of the right tunnel")
        print("you feel invigorated, the rune on the wall glows briefly.")
        break
    else:
        print("We need to pick a tunnel, not stand here nattering.")


"""
Forgot to mention you have a sword and a few trinkets. Press "I" to check your inventory.
[sword, unspooling string, glowing potion bottle, clothes-on-your-back, gold coins in brown envelope]
Excellent, lets get moving. I'll tell you more on the way

right
Rune embews player with extra attack strength x2

Mopey Goblin Encounter: 
You travel down the gloomey tunnels lit only by the Helpful Orb until you come to a corner with a bench 
hewn from the rockwall. Sat on the bench is a goblin, his head is downcast and he doesnt notice you. He 
appears to be sad. You notice he has a wicked looking axe in his hand which is drenched in blood, it drips
from the serrated black blade.
    - Ask if he is okay?
    - Sneak attack with your sword
    - Hurl the Helpful Orb at him
    - Take off your clothes
Ask if he's okay?
    Are you alright friend? 
    Mopey Goblin: The other Goblins soaked my axe in pigs blood as a joke and now it's disgusting. 
    I've just had a rubbish day, I'm alright really. Thanks for asking. Do you need something? 
        1a Just looking for the way out? - Mopey_Goblin gives bad advice
        2a No, I'm taking my orb for a walk. Hope your stuff all works out. - Mopey_Goblin goes back to moping
        3a I'll trade you this clean sword for that manky axe if you like? - Mopey_Goblin accepts trade
            Mopey_Goblin: 1a Oh just go back the way I came, take the second left after the screaming bulls head on 
                             the wall and head straight. Can't miss it
                          2a "Lovely orb. Have a nice walk." Begins to mop blood off the axe and ignores you.
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