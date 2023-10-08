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

airElemental = Character(data[7][1], data[7][2], data[7][3],
                         data[7][4], data[7][5], data[7][6], data[7][7],
                         data[7][8], data[7][9])

player.health = int(player.health)
player.defense = int(player.defense)
player.attack = int(player.attack)

deathCount = 0

# MECHANICAL FUNCTIONS


def inventory(Character):
    # inventory reveal function
    print(f'\nYou are armed with a {Character.weapon}, wearing ' +
          f'{Character.clothes} and carrying a {Character.item1}.' +
          f' There is a {Character.item2} in your pocket.\n')


def windsTear(Character):
    # picking up the air elementals tear bonus
    Character.defense = ((int(Character.defense)) * 3)
    print("\nThe tear instantly melts in your palm. You tingle.")
    print("There is a film of wind blowing over the surface of your body.")
    print("You feel better protected somehow.\n")


def rune(Character):
    # crossing over the doorway rune bonus
    Character.health = (Character.health) * 2


def takeUpAxe():
    # exchanging weapons for the goblin axe bonus
    player.attack = mopeyGoblin.attack
    player.weapon = mopeyGoblin.weapon


def tradeForChicken():
    player.item2 = "Chickenify Spell"


def noClothes(player):
    # removing clothes negative effect
    player.clothes = "nothing"
    player.defense = 0


def combat(Character1):
    # combat function used for all encounters except instant death endings
    enemyAttack = int(Character1.attack)
    enemyHealth = int(Character1.health)
    attackRemainder = enemyAttack - int(player.defense)
    if (enemyAttack > int(player.defense)):
        player.health = int(player.health) - attackRemainder
        if (player.health <= 0):
            return "dead"
        else:
            enemyHealth = enemyHealth - int(player.attack)
            if enemyHealth <= 0:
                return "win"
            else:
                combat(Character1)
    else:
        return "shrug"


def playerStats():
    # test code to be commented out before deployment but kept to troubleshoot
    # code reveals stats and helps to track issues
    print(f'\nPlayer stats H{player.health} D{player.defense}' +
          f' A{player.attack}\n')


# NARRATIVE FUNCTIONS
# player stats H50 A25 D25
def gameStart():
    print("\nYou wake to find yourself in a dark stone corridor, " +
          "the floor is sand.")
    print("The air is musty, in your hand a glowing sphere throbs gently.")
    print("The Orb pulses and a voice emanates from inside.\n")
    introOne()


def introOne():
    print("         :Helpful Orb:")
    print("Hello!")
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
                print("I love that name. Bob, Bob, Bob. I could " +
                      "say it all day.")
            print(f'\n{player.name}. Okay {player.name}, where are you from?')
            player.home = input(">")
            deathMemory()
            break
        elif memoryOfName.lower() in ["no", "n"]:
            print("\n         :Helpful Orb:")
            print(f"Okay, no stress. It's ummmm... {player.name}! Your name " +
                  f"is {player.name}. Yes.")
            print(f"And in case you're wondering you are from...{player.home}")
            deathMemory()
            break
        elif memoryOfName.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("\n         :Helpful Orb:")
            print("This is no time for weird answers. Just say yes or no.")


def dead():
    global deathCount
    print("\nYOU ARE DEAD")
    print(f'{player.name} from {player.home} is no more.')
    player.health = int(data[1][3])
    player.attack = int(data[1][4])
    player.defense = int(data[1][5])
    player.weapon = (data[1][6])
    player.clothes = (data[1][7])
    player.item1 = (data[1][8])
    player.item2 = (data[1][9])
    deathCount += 1
    while True:
        print("\nWould you like to try again? (yes/no)")
        tryAgain = input("> ")
        if tryAgain.lower() in ["yes", "y"]:
            introTwo()
            break
        elif tryAgain.lower() in ["no", "n"]:
            print(f'\nBut you only died {deathCount} times...')
            print(f'Goodbye {player.name}, the Labyrinth is not' +
                  f' for the faint of heart.')
            exit()
        elif tryAgain.lower() in ["i", "inventory"]:
            print("\nYou're dead. You don't have possessions.")
        else:
            print("You must choose.")


def effectivelyDead():
    global deathCount
    print("\nYOU ARE EFFECTIVELY DEAD")
    print(f'{player.name} from {player.home} is no more.')
    player.health = int(data[1][3])
    player.attack = int(data[1][4])
    player.defense = int(data[1][5])
    player.weapon = (data[1][6])
    player.clothes = (data[1][7])
    player.item1 = (data[1][8])
    player.item2 = (data[1][9])
    deathCount += 1
    while True:
        print("\nWould you like to try again? (yes/no)")
        tryAgain = input("> ")
        if tryAgain.lower() in ["yes", "y"]:
            introTwo()
            break
        elif tryAgain.lower() in ["no", "n"]:
            print(f'\nBut you only died {deathCount} times...')
            print(f'Goodbye {player.name}, the Labyrinth is not' +
                  f' for the faint of heart.')
            exit()
        elif tryAgain.lower() in ["i", "inventory"]:
            print("\nYou're dead. You don't have possessions.")
        else:
            print("You must choose.")


def readyOne():
    while True:
        print("\nAre you ready? (yes/no)")
        readyOne = input("> ")
        if readyOne.lower() in ["yes", "y"]:
            firstChoice()
            break
        elif readyOne.lower() in ["no", "n"]:
            print(f'\n{player.name}, we have to go at some point')
        elif readyOne.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("That doesn't mean anything to me.")


def proceed():
    while True:
        print("\n         :Helpful Orb:")
        print("Do you want to keep going? (yes/no)")
        proceedOption = input("> ")
        if proceedOption.lower() in ["yes", "y"]:
            print("There's a brave hero. On we go!")
            break
        elif proceedOption.lower() in ["no", "n"]:
            print("\n         :Helpful Orb:")
            print("There isn't really much choice here.")
            print("Only death lies behind. Freedom lies ahead.")
        elif proceedOption.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("\n         :Helpful Orb:")
            print("You just have to put one foot in front of the other.")


def defendOrFreeze():
    while True:
        print("\nDo you fight? (yes/no)")
        defendOrFreezeChoice = input("> ")
        if defendOrFreezeChoice.lower() in ["yes", "y"]:
            break
        elif defendOrFreezeChoice.lower() in ["no", "n"]:
            print("Your arms go weak, you freeze with fear.")
            break
        elif defendOrFreezeChoice.lower() in ["i", "inventory"]:
            print("No time for that.")
            break
        else:
            print("You aren't thinking clearly.")
            break


def introTwo():
    print("\nYou wake to find yourself in a dark stone corridor again," +
          " the floor is the same sand.")
    print("The air is just as musty as last time, in your hand the" +
          " glowing sphere throbs gently.")
    print("The Orb pulses and speaks.")
    print("\n         :Helpful Orb:")
    print(f'Hi again {player.name}. Even I remember what just happened.')
    print("Or at least did...will...has happened. Doesn't matter.")
    print("Brutal, just brutal. Need a minute to shake that off.")
    print("The Labyrinth seems to respawn you at this moment in time.")
    print("Let's go again. This time we'll be extra careful.")
    readyOne()


def deathMemory():
    print(f'\nWell {player.name} this whole situation may seem a little' +
          f' disconcerting at first.')
    while True:
        print("Do you remember anything? (yes/no) ")
        playerRemembers = input("> ")
        if playerRemembers.lower() in ["yes", "y"]:
            print("\n         :Helpful Orb:")
            print("You probably already died at least once then.")
            print("The Labyrinth seems to respawn you at this moment in time.")
            print("Oh well, at least I don't need to go over anything.")
            print("Lets try not to do whatever it was we did before.")
            readyOne()
            break
        elif playerRemembers.lower() in ["no", "n"]:
            print("\n         :Helpful Orb:")
            print("I thought you mightn't. I'm The Orb of Helping.")
            print("You came to this danger filled labyrinth,")
            print("to find an ancient relic. You found it... me!")
            print("Then you... we set off a booby-trap,")
            print("which appears to have given you mild magical amnesia.")
            print("We are lost, currently escaping, and now you're all " +
                  "caught up.")
            readyOne()
            break
        elif playerRemembers.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("\n         :Helpful Orb:")
            print("Oh you've gone mad... I was worried this would happen.")
            print("I'll speak slower.")


def firstChoice():
    print("\n     -You proceed into the labyrinth-")
    print("There is a fork in the tunnel ahead.")
    print("The right path has a rune enscribed on the wall.")
    print("The left path has fresher smelling air.")
    while True:
        print("\nDo you choose to go left or right? (L/R) ")
        firstChoice = input("> ")
        if firstChoice.lower() in ["left", "l"]:
            ("\nYou've decided to take the left tunnel.")
            playerStats()
            airElementalEncounter()
            break
        elif firstChoice.lower() in ["right", "r"]:
            print("\nYou've decided to take the right tunnel.")
            while True:
                print("\nWill you duck under the rune on the wall? (yes/no)")
                duckRune = input("> ")
                if duckRune.lower() in ["no", "n"]:
                    print("\nYou cross the threshold of the right tunnel")
                    print("You feel invigorated as the rune on the " +
                          "wall glows briefly.")
                    rune(player)
                    playerStats()
                    goblinEncounterFunc()
                    break
                elif duckRune.lower() in ["yes", "y"]:
                    print("You duck beneath the rune cautiously.")
                    playerStats()
                    goblinEncounterFunc()
                    break
                else:
                    print("There's no turning back now.")
            break
        elif firstChoice.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("We need to pick a tunnel, not stand here nattering.")


def airElementalEncounter():
    # Air Elemental Stats H25 A75
    print("\n     -You proceed further into the Labyrinth-")
    print("There is a rushing sound of wind ahead.")
    print("You turn a corner to find a being of pure air facing you.")
    print("Grains of sand from the floor swirling across the surface" +
          " of a humanoid shape.")
    print("The Air Elemental gusts towards you.")
    defendOrFreeze()
    elementalFight = combat(airElemental)
    if elementalFight == "dead":
        print("The orb is knocked from your grasp, light streams" +
              " up from below.")
        print("You are pressed against the wall and pinned in place.")
        print("Like the mountains at the edge of a windswept desert.")
        print("You are sandblasted until there is nothing left but dust.")
        dead()
    elif elementalFight == "win":
        print("You raise your sword and gulp a breath of air.")
        print("You feel the wind buffeting your face and eroding your skin.")
        print("But you landed a hit!")
        print("The blowing sands cease and fall to the ground.")
        print("The Air Elemental has met its end at the tip of your blade.")
        print("A tear drop of steaming dry ice lays on the ground.")
        windsTear(player)
        proceed()
        nakedWizardEncounter()
    else:
        print("You shrug off the feeble wind and push past it.")
        print("You are on a quest and nothing shall stop you.")
        print("The Air Elemental is embarrassed and hurries away" +
              " down the tunnels.")
        nakedWizardEncounter()


def goblinEncounterFunc():
    # Mopey Goblin stats H20 A100
    print("\n     -You proceed further into the Labyrinth-")
    print("Light comes only from the Helpful Orb")
    print("You round a corner to find a bench up ahead hewn " +
          "into the rock wall.")
    print("Sat on the bench is a goblin, his head is downcast, he looks sad.")
    print("He hasn't noticed you yet.")
    print("A wicked looking axe in his hand is drenched in blood; it drips.\n")
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
            print("Other Gobbos soaked my choppa in pigs blood, it's ruined.")
            print("Just having a rubbish day, I is alright.")
            print("Thanks for asking. Do you need something humie?")
            goblinsQuestionFunc()
            break
        elif mopeyGoblinEncounter.lower() in ["2", "two"]:
            print("\nYou draw your sword and creep towards the creature.")
            print("As you approach, you hear the Helpful Orb" +
                  " hold it's breath.")
            goblinFight = combat(mopeyGoblin)
            if goblinFight == "win":
                print("The Goblin looks up at the sound and snarls at you.")
                print(f'You are lightning fast, your {player.weapon}' +
                      f' flashes right.')
                print("The goblin tries to parry but the blow knocks" +
                      " him against the wall.")
                print("He clumsily raises the axe above his head and" +
                      " you slash across his upraised arms.")
                print("The limbs drops to the floor with the axe" +
                      " still gripped tightly.")
                print("The Goblin steps back; shocked.")
                print("Then collapses, defeated.\n")
                print("         :Mopey Goblin:")
                print('What a rubbish day.\n')
                print("The goblin lies still.")
                lootGoblin()
            elif goblinFight == "dead":
                print("The goblin hears the intake of breath.")
                print("He lurches towards you.")
                print("You swing to strike but he powerslides" +
                      " underneath the blow")
                print("You feel the weight of the axe embbed" +
                      " itself in your spine.")
                print("A brave attempt.")
                dead()
            else:
                print("He spots you approaching and rushes to engage.")
                print("You take a blow from his axe to your shoulder.")
                print("You shrug off the puny attempt at violence" +
                      " and stare him down.")
                print("The goblin squeals and clutches his cheast.")
                print("He has died of fright")
                lootGoblin()
        elif mopeyGoblinEncounter.lower() in ["3", "three"]:
            print("\nYou decide upon shock and awe.")
            print('"Bold!" you think as you strip down in the dark tunnel.')
            print('"Come out swinging" you say to yourself.')
            print("The Goblin is not expecting a nude human.")
            print("Your flailing arms and screaming is off putting.")
            print("However the hallway is long and he's holding an axe.")
            print("He hurls the axe at your unarmoured chest.")
            print("You catch the axe dead center mass.")
            print("This is a quick death.")
            print("What were you expecting?")
            dead()
        elif mopeyGoblinEncounter.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("\nOnly death lies behind")
            print("You must choose.")


def lootGoblin():
    while True:
        print("\nWould you like to swap weapons for his axe? (yes/no)")
        collectAxe = input("> ")
        if collectAxe.lower() in ["yes", "y"]:
            print("\nThe bloody choppa will do great things in your hands.")
            print(f'You drop the {player.weapon}, and take up the axe.')
            takeUpAxe()
            turnBack()
        elif collectAxe.lower() in ["no", "n"]:
            print("\nYou think better than to touch the axe.")
            turnBack()
        elif collectAxe.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("\nThat doesn't answer the question.")


def turnBack():
    print("You hear ominous laughing in the corridor ahead")
    print("\n         :Helpful Orb:")
    print("That doesn't sound good. Go back!\n")
    print("1-Run back the way you came.")
    print("2-Carefully carry on ahead")
    turnBack1 = input("> ")
    if turnBack1.lower() in ["1", "one"]:
        print("You hurry back to the turn and take the left tunnel.")
        airElementalEncounter()
    elif turnBack1.lower() in ["2", "two"]:
        print("You gingerly carry on towards the laughter.")
        goblinGang()
    else:
        print("You spend too long thinking.")
        goblinGang()


def goblinGang():
    print("\nRunning towards you down the tunnel is a gang " +
          "of chattering Goblins.")
    print("They seem much cheerier than your last encounter " +
          "and are all heavily armed.")
    print("Before you can ask how they are feeling," +
          " a blow dart impacts your neck.")
    print("You feel the poison burning. You have seconds to live.")
    goblinDeathChoice()


def goblinsQuestionFunc():
    while True:
        print('\n1- "Just looking for the way out mate?"')
        print('2- "No, I am taking my orb for a walk. Hope your stuff all' +
              ' works out."')
        print('3- "I will trade you this clean sword for that dirty axe if' +
              ' you like?"')
        print('Enter the number of your choice')
        mopeyGoblinQuestion = input("> ")
        if mopeyGoblinQuestion.lower() in ["1", "one"]:
            print(f"\n           :{player.name}:")
            print("Just looking for the way out mate?")
            print("\n            :Mopey Goblin:")
            print("Oh right... well just carry on along this tunnel.")
            print("When you come to the screaming bulls head on the wall,")
            print("Hang a left and head staight. Cant miss it.\n")
            print("You hurry off down the corridor.")
            print("As you find a groteque bulls head on the " +
                  "wall. Cackles sound nearby")
            print("The echoes make it impossible to locate the source")
            print("You sprint down the corridor to the left")
            goblinGang()
            break
        elif mopeyGoblinQuestion.lower() in ["2", "two"]:
            print(f"\n           :{player.name}:")
            print("No, I am taking my orb for a walk. Hope your stuff all" +
                  " works out.")
            print("\n          :Mopey Goblin:")
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
            dead()
            break
        elif mopeyGoblinQuestion.lower() in ["3", "three"]:
            print(f"\n           :{player.name}:")
            print(f"Care to trade your axe for my clean {player.weapon}?")
            print("\n          :Mopey Goblin:")
            print("Really?!That would be great actually. Here you go")
            takeUpAxe()
            print("Just needs a wipe, thats all")
            print("I wouldn't hang about, the others arent keen on humans.")
            print("You seem like one of the good ones. Go back " +
                  "the way you came")
            while True:
                print("Do you trust the Goblin? (yes/no)")
                trustGoblin = input("> ")
                if trustGoblin.lower() in ["yes", "y"]:
                    print(f"\n           :{player.name}:")
                    print("Thank you friend, good luck.")
                    print("\nYou hurry back the way you came.")
                    print("Bringing you back to the left tunnel.")
                    print("You carry on towards the sound of rushing air.")
                    airElementalEncounter()
                    break
                elif trustGoblin.lower() in ["no", "n"]:
                    print(f"\n           :{player.name}:")
                    print("Appreciate the advice, but we'll take our chances.")
                    print("\n          :Mopey Goblin:")
                    print("Suit yourself. See you next time.")
                    print("\nYou confidently continue on down the corridor" +
                          " for some time.")
                    goblinGang()
                    break
                elif trustGoblin.lower() in ["i", "inventory"]:
                    inventory(player)
                else:
                    print("Well, what is your gut telling you?")
            break
        elif mopeyGoblinQuestion.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("The Mopey Goblin stares at you intently, waiting.")


def goblinDeathChoice():
    while True:
        print("\n1- drink the potion in your pocket")
        print("2- throw the Orb of Helping at the goblin gang")
        print('Enter the number of your choice')
        goblinDeathChoice = input("> ")
        if goblinDeathChoice.lower() in ["1", "one"]:
            print("\nYou scrabble for the vial in your pocket" +
                  " and gulp the elixir")
            print("Your hands tingle, they swell and begin to grow.")
            print("You die with massive hands and goblins laughing" +
                  " hysterically around you as your face goes purple.")
            dead()
        elif goblinDeathChoice.lower() in ["2", "two"]:
            print("\nYou hurl the screaming orb at the largest goblin")
            print("Your only friend and source of light smashes and curses" +
                  " your name")
            print("You die in darkness as goblins cackle and crowd in")
            dead()
        else:
            print(f'You shout "{goblinDeathChoice}", which means nothing to' +
                  ' anyone but you.')
            print("The poison dart works quickly")
            print("You die in the tunnels. The Helpful Orb weeps for you.")
            dead()


def nakedWizardEncounter():
    print("\n     -You proceed into the labyrinth-")
    print("The tunnel grows wider until it joins with a circular chamber.")
    print("At the centre of the chamber a massive column holds the ceiling.")
    print("As you stare at the strange cavern architecture,")
    print("A face peers round from behind the column.")
    print("It is a tall man wearing a pointy hat.")
    print("\n         :Grand Wizard Methielteez:")
    print("Ah you're here! At last!")
    print("I expect it took you quite a few deaths to get this far.")
    print("It certainly took me more than a few.")
    print("Funny what that can do to the mind after a while," +
          " makes one forgetful")
    print("\nHe steps out further from behind the column.")
    print("The wizard appears to have forgotten to dress himself.")
    print("\n         :Grand Wizard Methielteez:")
    print("It's hard at first, living in the labyrinth, " +
          "but you'll get used to it")
    print("\n1-Attack the Wizard!")
    print("2-Offer to trade your potion with him for something of value")
    print("3-Offer to give him your clothes as a gift")
    while True:
        wizardsChoice = input("> ")
        if wizardsChoice.lower() in ["1", "one"]:
            print("\nYou get bad vibes from the naked wizard.")
            print("Attack is the only option. He must be trying to trick you")
            wizardFight = combat(nakedWizard)
            if wizardFight == "win":
                print("This shouldn't happen.")
                print("The wizard is a non-combat win scenario")
                dead()
            elif wizardFight == "dead":
                print(f"\nYou rush the forgetful archanist, " +
                        f"{player.weapon} raised to strike.")
                print("However you fail to spot his hands.")
                print("The wizard whips open a scroll of paper " +
                        "and whispers a word.")
                print("You see the image of a chicken flash in the air.")
                print("The world grows as feathers sprout from your skin.")
                print("For a moment, it is agony, then your mind is calm.")
                print("You are a chicken. You aren't worried " +
                        "about anything.")
                print("\n         :Grand Wizard Methielteez:")
                print(f"Come on little {player.name}, I've been dying" +
                        " for some nuggets.")
                effectivelyDead()
            else:
                print("You both charge. Then draw back." +
                        " No one will win this fight.")
                print("You nod at each other and he points to a tunnel")
                secretTunnel()
            break
        elif wizardsChoice.lower() in ["2", "two"]:
            print(f"\n           :{player.name}:")
            print("Always good to meet a fellow traveller. " +
                  " Perhaps a trade? I have this potion.")
            print("\n         :Grand Wizard Methielteez:")
            print("A vial of Enlarge Hands! An unusual elixir indeed.")
            print("Let me see what I have around here. Ah how about this?")
            print("I have a scroll containing the spell Chickenify.")
            while True:
                print("Do you want the power to Chickenify someone? (yes/no)")
                chickenifyOffer = input("> ")
                if chickenifyOffer.lower() in ["yes", "y"]:
                    print(f"\n           :{player.name}:")
                    print("Alright, sounds like a fair trade.")
                    tradeForChicken()
                    break
                elif chickenifyOffer.lower() in ["no", "n"]:
                    print()
                    break
                elif wizardsChoice.lower() in ["i", "inventory"]:
                    inventory(player)
                else:
                    print("I'm not sure what you mean. The offer stands.")
            break
        elif wizardsChoice.lower() in ["3", "three"]:
            print()
            break
        elif wizardsChoice.lower() in ["i", "inventory"]:
            inventory(player)
        else:
            print("You blurt out a weird sound and" +
                  " the wizard waits unsurprised.")


# GAME START

print("__   __                             _         _   _                   ")
print("\ \ / /                            (_)       | | | |                  ")
print(" \ V /___  _   _    __ _ _ __ ___   _ _ __   | |_| |__   ___          ")
print("  \ // _ \| | | |  / _` | '__/ _ \ | | '_ \  | __| '_ \ / _ \         ")
print("  | | (_) | |_| | | (_| | | |  __/ | | | | | | |_| | | |  __/         ")
print("  \_/\___/ \__,_|  \__,_|_|  \___| |_|_| |_|  \__|_| |_|\___|         ")
print("______    _        _   _           _                _       _   _     ")
print("|  ___|  | |      | | | |         | |              (_)     | | | |    ")
print("| |_ __ _| |_ __ _| | | |     __ _| |__  _   _ _ __ _ _ __ | |_| |__  ")
print("|  _/ _` | __/ _` | | | |    / _` | '_ \| | | | '__| | '_ \| __| '_ \ ")
print("| || (_| | || (_| | | | |___| (_| | |_) | |_| | |  | | | | | |_| | | |")
print("\_| \__,_|\__\__,_|_| \_____/\__,_|_.__/ \__, |_|  |_|_| |_|\__|_| |_|")
print("                                          __/ |                       ")
print("                                         |___/                        ")

gameStart()

exit()

"""

That would be really great. Here you go,
it's a brilliant axe once you've cleaned it.
Thank you. I wouldn't hang about, the others
arent keen on humans. You seem like one of
the good ones though

"""
