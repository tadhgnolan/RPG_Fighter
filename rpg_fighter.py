"""
Module and authorization credentials for Google Sheets API.
Needed to store inputs and retrieve NPC Stats.
Main code structure taken from Love Sandwitches by Code Institute
(See Readme for link to repo.).
"""

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


NPC_STATS = []


def get_character_race():
    """
    Get npc character race input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 values.
    The loop will repeatedly request data until it is valid.
    """
    while True:
        print("#  (    )  #")
        print("#  |\^^/|  #")  # noqa
        print("#  (0::0)  #")
        print("#   \\\//   #")  # noqa
        print("#   (OO)   #")
        print("#    \/    #")  # noqa
        print("RPG Fighter, a tabletop RPG tool by Tadhg Nolan")
        print("Please enter NPC character race.")
        print("Data should be 6 npc race names.")
        print(
            "Example: orc, goblin, halfling, troll, "
            + "dwarf, skeleton, elf, human\n"
        )

        data_str = ""
        for i in range(6):
            while True:
                user_npc = (
                    input(f"Enter npc race #{i + 1} here:\n")
                    .lower()
                    .strip()
                )
                races = [
                    "orc",
                    "halfling",
                    "goblin",
                    "troll",
                    "dwarf",
                    "skeleton",
                    "elf",
                    "human",
                ]
                if user_npc not in races:
                    print("Invalid race, try again.")
                else:
                    if i <= 4:
                        data_str += user_npc + ","
                        break
                    else:
                        data_str += user_npc
                        break

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


def get_last_entry_character_race(npc):
    """
    Collect last row of data from NPCs worksheet returning the data as a list
    """
    npc_races = SHEET.worksheet("npc_stats")
    columns = []
    for ind in range(1, 10):
        column = npc_races.col_values(ind)
        if npc.lower().strip() == column[0].lower().strip():

            NPC_STATS.append(column)
            columns.append(column[-1:])

    return columns


def display_stats():
    """
    Displays NPC Stats in an easy to read manner.
    """
    for npc in NPC_STATS:
        print(f"Race: {npc[0]}")
        print(f"Strength: {npc[1]}")
        print(f"Dexterity: {npc[2]}")
        print(f"Constituion: {npc[3]}")
        print(f"Intelligence: {npc[4]}")
        print(f"Wisdom: {npc[5]}")
        print(f"Charisma: {npc[6]}")
        print("")


def main():
    """
    Run all program functions
    """
    while True:
        data = get_character_race()
        update_npc_worksheet(data)
        for npc in data:
            get_last_entry_character_race(npc)
        display_stats()
        check = input(
            "Do you wish to quit or start again?"
            + " Enter Y to restart or another key to exit: "
        )
        if check.upper() == "Y":  # go back to the top
            continue
        print("Thanks for using the RPG Fighter, goodbye!")
        break  # exit


if __name__ == "__main__":
    print("Welcome to RPG_Fighter NPC Generator")
    main()
