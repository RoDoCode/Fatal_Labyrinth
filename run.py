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
name = input("Welcome user, please enter your name")

print("Well " + name + ", we have a lot of work to do")

origin_location = input("Where are you are you from?")

print("Good place to start a story. I was manufactured in the town just North of " + origin_location)

supplies = input("But I digress and we don't have much time. Do you have money and a weapon? Yes or no?")

print(supplies);

"""

if supplies == "yes" or "Yes": print("Excellent, lets get moving. I'll tell you more on the way")
elif supplies == "no" or "No": print("Then we better tool up. Look around for a weapon.")
else: print("This is no time to mess around " + name + " from " + origin_location)