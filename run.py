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
    - Thats a relief. I don't need to go over anything then. Let's push on.
    - I thought you mightn't. I'm The Orb of Helping. 
      You brought me to this danger filled labyrinth to help you 
      find an ancient relic. We set off a booby-trap which appears
      to have given you mild magical amnesia. We are lost, currently
      escaping, and now you're caught up.
A fork in the tunnel ahead, right ot left? 
(right has a run on the wall, left the air smells fresher) -forkOne
Forgot to mention you have a sword and a few trinkets. Press "I" to check your inventory.

Excellent, lets get moving. I'll tell you more on the way
Then we better tool up. Look around for a weapon.
This is no time to mess around " + playerName 

"""