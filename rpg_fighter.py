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
SHEET = GSPREAD_CLIENT.open('RPGFighter')


def get_character_race():
    """
    Get npc character race input from the user
    """
    print("Please enter npc character race.")
    print("Data should be DnD race name, seperated by commas.")
    print("Example: Orc, Dragonborn, bugbear, skeleton\n")

    data_str = input("Enter npc races here: ")
    print(f"The npc races you provided were {data_str}")


get_character_race()
