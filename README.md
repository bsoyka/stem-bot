# STEM Bot
This Discord bot exists to help with problems related to Science, Technology, Engineering, and Math.

## Table of Contents
- [STEM Bot](#stem-bot)
  - [Table of Contents](#table-of-contents)
  - [Commands](#commands)
    - [Science](#science)
    - [Mathematics](#mathematics)
    - [Utilities](#utilities)
  - [Setting up a Dev Environment](#setting-up-a-dev-environment)
    - [Installing Dependencies](#installing-dependencies)
    - [Setting up the Submodule](#setting-up-the-submodule)
      - [Setting up When Cloning the Repo](#setting-up-when-cloning-the-repo)
      - [Setting up after Cloning the Repo](#setting-up-after-cloning-the-repo)
    - [Setting up a Bot Account on Discord](#setting-up-a-bot-account-on-discord)
    - [Running the Bot](#running-the-bot)

## Commands
### Science
* `element`: Get a specific element by atomic number, symbol, or name
  * Aliases: `e`, `el`, `elem`
  * Arguments:
    * `element_input`: An atomic number, element symbol, or element name

### Mathematics
* `sigfigs`: Round a number to a specified number of significant figures
  * Aliases: `sf`, `sfs`
  * Arguments:
    * `number`: Number to round
    * `figures`: Number of significant figures to round to

### Utilities
* `ping`: Check the bot's latency
  * Aliases: `pong`
  * Arguments: *None*
* `wikipedia`: Get a summary from Wikipedia
  * Aliases: `w`, `wp`, `wikipedia`
  * Arguments:
    * `search_term`: What to search for
* `steal`: Steal a custom emoji
  * Aliases: *None*
  * Arguments: *None*
  * Permissions required:
    * User:
      * `add_reactions`
      * `external_emojis`
      * `manage_emojis`
    * Bot:
      * `manage_emojis`

## Setting up a Dev Environment
### Installing Dependencies
```
python -m pip install -r requirements.txt
```
### Setting up the Submodule
The bot uses the [Bowserinator/Periodic-Table-JSON](https://github.com/Bowserinator/Periodic-Table-JSON) repo to retrieve periodic table info. This is done using [Git Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules). Put simply, this allows us to bring the periodic table repo into this one.

You have two main options to initialize and update submodules. You can choose to set this up at the time of cloning either this repo or your own fork, or you can set this up after with a simple command.
#### Setting up When Cloning the Repo
```
git clone --recurse-submodules https://github.com/username/reponame
```
#### Setting up after Cloning the Repo
```
git submodule update --init
```
### Setting up a Bot Account on Discord
For the bot to run, it has to have an account on Discord. You can make this happen using these simple steps:
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application (You'll need to give it a name). Take note of the Client ID given to your application.
2. Add a bot user to the application in the `Bot` menu. Reveal the token and save it as an environment variable in your system named `SCIBOT_TOKEN`.
3. You may want to disable the `Public Bot` option if you're just going to use this bot user for development and testing. This setting allows anyone to add your bot to their server.
4. Add the bot to a server, preferably one just for development and testing. You can use this link, making sure to add in the Client ID for your bot:
```
https://discordapp.com/oauth2/authorize?client_id=INSERT_CLIENT_ID_HERE&scope=bot&permissions=1073769472
```
### Running the Bot
If you've already added the bot token to the `SCIBOT_TOKEN` environment variable, you can start up the bot by running the `main.py` file:
```
python main.py
```
If all goes well, you'll see a message in your terminal saying something along the lines of `Logged in as botusername#1234`. Your bot will also have an online status on Discord, likely with a custom status like `Playing with elements`.