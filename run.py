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
print(data)

"""
name = input("Hello again, do you remember your name?")
print("Good start. Well " + name + ", this whole situation may seem a little disconcerting at first.")
player_remembers = input("Do you remember what happened a moment ago?")
print("Thats a relief. I don't need to go over anything then. Let's push on.)
supplies = input("But I digress and we don't have much time. Do you have money and a weapon? Yes or no?")
print(supplies);
if supplies == "yes" or "Yes": print("Excellent, lets get moving. I'll tell you more on the way")
elif supplies == "no" or "No": print("Then we better tool up. Look around for a weapon.")
else: print("This is no time to mess around " + name + " from " + origin_location)

"""
"""
Hello again, do you remember your name? - playerName
Good start. 
And where are you from? -playerHome
Well -playerName- this whole situation may seem a little disconcerting at first.
Do you remember what happened a moment ago? - playerRemembers
    - You probably already died at least once then. Oh well I don't need to go 
    over anything then. Lets try not to do whatever it was we did before. Onward!
    - I thought you mightn't. I'm The Orb of Helping. 
      You brought me to this danger filled labyrinth to help you 
      find an ancient relic. We set off a booby-trap which appears
      to have given you mild magical amnesia. We are lost, currently
      escaping, and now you're caught up.
There's a fork in the tunnel ahead, right ot left? 
(right has a rune on the wall, left the air smells fresher) -forkOne
Forgot to mention you have a sword and a few trinkets. Press "I" to check your inventory.
[sword, unspooling string, glowing potion bottle, clothes-on-your-back, gold coins in brown envelope]
Excellent, lets get moving. I'll tell you more on the way

right
Rune embews player with extra attack strength x2
When you cross the threshold of the right tunnel you feel invigorated, the rune on the wall glows briefly.
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