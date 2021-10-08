import requests
import random

username = input("username: ")
with open("token.txt") as file:
    while (line := file.readline().rstrip()):
        headers = {
    'authorization': f"{line}"
    }
        r = requests.put(f"https://api.spotify.com/v1/me/following?type=user&ids={username}", headers=headers)
        print(r.status_code) 
