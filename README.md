# RPG FIGHTER

![Device Mockup Image](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/mockup.png)
![RPG Fighter live example](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/demo.gif)
# Table of Contents
1. [Intro](#intro)
2. [Technologies](#Technologies)
3. [Features](#features)
4. [Testing](#testing)
5. [Credits](#credits)
6. [Deployment](deployment)

## Intro

RPG Fighter is a app for tabletop roleplaying game Dungeon Masters or players that allows them to retrieve a list of statistic scores (stats) for a set of Non-Player-Characters (NPCs) by name.

## UX


## User Stories

### New Site Users

- As site user, I would like clear instructions on how to use the app.
- As a site user, I would like to be able to input a selection of Non-Player-Characters (NPCs).
- As a site user, I would like confirmation that the worksheet has been updated with the data I've entered, so that I can be sure I will receive the correct response.
- As a site user, I would like to see the full list of details for the NPC names that I've entered, so that I can take note of them for the game I'm planning.
- As a site user, I would like to be asked if I wish to continue, so that I can either start again or exit the app.

## Wireframes

![wireframe1](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/wf1.png)
![wireframe2](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/wf2.png)
![wireframe3](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/wf3.png)

## Features

### Existing Features

- **Get Character Race**

    - Function prints a welcome message and instructions, then takes input of user_npc and while loop checks that 6 inputs are made matching the pre-existing list of NPCs.

![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/feature01.png)
![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/feature01.1.png)
![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/feature01.2.png)

- **Validate Data**

    - Inside the try, function raises ValueError if there aren't exactly 6 values 

![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/feature02.png)
![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/feature02.1.png)

- **Update NPC Worksheet**

    - Function takes character_race list and adds it to worksheet as a new row.

![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/feature03.png)
![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/feature03.1.png)

- **Get Last Entry Character Race**

    - Function collects last row of data from NPCs worksheet and returns the data as a list.

![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/feature04.png)

- **Display State**

    - Function prints stats for each NPC in an easily readable format.

![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/feature05.png)
![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/feature05.1.png)

- **Main**

    - Runs all program functions.

![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/feature06.png)

### Future Features

- Random Player Character Generator
    - Creates a player character with a random set of stats.
- Random NPC Generator
    - Creates an NPC with a ranpm set of stats
- Fight
    - Functions that allow Player Character to fight NPC through application of random dice rolls and their interaction with a clearly defined ruleset.

## Technologies

- [Python](https://www.python.org) used as the back-end programming language.
- [Git](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [GitHub](https://github.com) used for secure online code storage.
- [Gitpod](https://gitpod.io) used as a cloud-based IDE for development.
- [Heroku](https://www.heroku.com) used for hosting the deployed back-end site.
- [Google_Docs](https://docs.google.com/) used to host the data used in the app.
- [MockIt App](https://mockittapp.wondershare.com/) used to create wireframes.
- [Lucid App](https://lucid.app/) used to create flowchart.


## Data Model

### Flowchart

![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/flowchart.png)

### Classes & Functions

The program uses classes as a blueprint for the project's objects (OOP). This allows for the object to be reusable.

```python
class Person:
    """ Insert docstring comments here """
    def __init__(self, name, age, health, inventory):
        self.name = name
        self.age = age
        self.health = health
        self.inventory = inventory
```

The primary functions used on this application are:

- `get_character_race()`
    - Get character race from the user.
- `validate_data()`
    - Checks that user has entered 6 values.
- `update_npc_worksheet()`
    - Update the relevant worksheet with the data provided.
- `get_last_entry_character_race(npc)`
    - Collects last row of data from NPCs worksheet.
- `display_stats()`
    - Displays NPC Stats.
- `main()`
    - Run all program functions.

### Imports

I've used the following Python packages and/or external imported packages.

- `gspread`: used with the Google Sheets API
- `google.oauth2.service_account`: used for the Google Sheets API credentials
- `unittest`: used with the unittest API

## Testing

- Manual testing of user inputs.

![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/manual_test1.png)
![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/manual_test2.png)
![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/manual_test3.png)

- Automated testing of validate function with Unittest.

![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/unittest1.png)
![screenshot](https://github.com/tadhgnolan/RPG_Fighter/blob/main/documentation/images/unittest2.png)

## Deployment

Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser.
This is to improve the accessibility of the project to others.

The live deployed application can be found deployed on [Heroku](https://rpg-fighter.herokuapp.com).

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- If using any confidential credentials, such as CREDS.JSON, then these should be pasted in the Config Variables as well.
- Further down, to support dependencies, select **Add Buildpack**.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your own GitHub repository to the newly created app:

Either:
- Select **Automatic Deployment** from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a app_name` (replace *app_name* with your app name)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type:
	- `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku!

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

If using any confidential credentials, such as `CREDS.json` or `env.py` data, these will need to be manually added to your own newly created project as well.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/tadhgnolan/RPG_Fighter) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
	- `git clone https://github.com/tadhgnolan/RPG_Fighter.git`
7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/tadhgnolan/RPG_Fighter)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/tadhgnolan/RPG_Fighter)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

## Credits



### Content

| Source | Location | Notes |
| --- | --- | --- |
| [Markdown Builder](https://traveltimn.github.io/markdown-builder) | README and TESTING | tool to help generate the Markdown files |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | version control | "How to Write a Git Commit Message" |
| [Editor.md](https://pandao.github.io/editor.md/index.html) | README.MD| open source online Markdown Editor |
| [Code Institute](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1) | rpg_fighter.py | Love Sandwitches repo on Github
| [Juan Carlos Paco](https://gist.github.com/juancarlospaco/040fbe326631e638f2a540fe8c1f2092) | test_rpg_fighter.py | unittest doctests template |

### Media
| Source | Location |
| --- | --- |
| [Artscene](http://artscene.textfiles.com/asciiart/dragon.txt) | Dragon head ASCII art. |
### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for their support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Slack community](https://code-institute-room.slack.com) for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my partner Rossana, for believing in me, and allowing me to make this transition into software development.
- I would like to thank my brother Cormac, a working developer, for his help reviewing the project.
