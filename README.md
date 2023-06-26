# Riot API Key Retrieval Tutorial

This tutorial provides step-by-step instructions on how to retrieve your Riot API key for accessing the League of Legends API. The API key is required to make API requests and retrieve game data.

## Disclaimer

This does only work if your game is in the following directory: C:\Riot Games\League of Legends\Game. I will include custom directories in the future.

## Is this a virus?

Surely not! If you are worried you can always run this via the python script. Feel free to scan the .exe at VirusTotal. My virus scanner does indeed block the execution of the .exe file.

## Why should you use this?

This process is unrelated to the launcher, so your online status does not change, and you don't even have to be logged in. Furthermore, this method still works even if spectating is bugged in the launcher.


## Steps to Retrieve Riot API Key

1. Visit the [Riot Developer Portal](https://developer.riotgames.com/) in your web browser.

2. Log in with your Riot Account.

3. Create an App api key by hovering over your Riot Name in the top right corner and clicking on 'APPS'.

4. After creating a app with some addtional data (name, purpose), you will have to wait some time until the key is activated.

5. Keep in mind that you can easily create a 24 hour expiration key on your [dashboard](https://developer.riotgames.com/).

6. Paste your gathered api key into the api_key.txt. Make sure to not include any additional symbols or white space.

7. You can now run the exe file or run the python script. Keep in mind that you will need to install riotwatcher (pip install [riotwatcher](https://riot-watcher.readthedocs.io/en/latest/)) if you want to use the python script.
