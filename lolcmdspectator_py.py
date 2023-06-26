import subprocess
import io
import sys
from riotwatcher import LolWatcher, ApiError

def error(*args):
    for msg in args:
        print(msg)
    input('Press any key to exit...')
    sys.exit()

try:
    key = io.open('api_key.txt', 'r', encoding='utf-8').read()
except FileNotFoundError:
    error('The api_key.txt file was not found. Please make sure to create the file and paste your API key into it.')

if key == '':
    error('There is something wrong with your api_key.txt file. Please make sure to paste the key correctly into the file.')

api = LolWatcher(key)

try:
    api.summoner.by_name('euw1', 'Hook the Duck')
except Exception:
    error('There is something wrong with your API key. Refer to the README file for more information.')
    sys.exit()

summonerName = input('Please enter the summoner name: ')

try:
    summoner = api.summoner.by_name('euw1', summonerName)
    spectation = api.spectator.by_summoner('euw1', summoner['id'])
    gameId = spectation['gameId']
    encryptionKey = spectation['observers']['encryptionKey']

    command = f'cd /d "C:\Riot Games\League of Legends\Game" & "League of Legends.exe" "spectator spectator-consumer.euw1.lol.pvp.net:80 {encryptionKey} {gameId} EUW1" "-UseRads"'
    subprocess.Popen(command, shell=True)

    print(f'Successfully started spectating {summonerName}!')
except ApiError as e:
    if e.response.status_code == 404:
        error(f'Summoner "{summonerName}" not found or not in an active game.')
    else:
        error('An API error occurred. Please try again later.')
