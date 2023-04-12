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
    Get npc character race input from the user.
    Run a while loop to collect a valid string of data from the user via the terminal, which must be a string of 6 values seperated by commas. The loop will repeatedly request data until it is valid.
    """
    while True:
        print("Please enter npc character race.")
        print("Data should be 6 DnD race names, seperated by commas.")
        print("Example: Orc, Dragonborn, bugbear, skeleton\n")

        data_str = input("Enter npc races here: ")

        character_race = data_str.split(",")

        if validate_data(character_race):
            print("Data is valid!")
            break

    return character_race


def validate_data(values):
    """
    Inside the try, raises ValueError if there aren't exactly 6 values.
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def update_npc_worksheet(data):
    """
    Update NPC worksheet, add new row with the list data provided.
    """
    print("Updating NPC worksheet...\n ")
    npc_worksheet = SHEET.worksheet("npcs")
    npc_worksheet.append_row(data)
    print("NPC worksheet updated successfully.\n")


data = get_character_race()
update_npc_worksheet(data)
