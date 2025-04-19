import os
import requests
from dotenv import load_dotenv

load_dotenv()

env = os.environ

BASE_URL = "https://api.artsy.net/api"
token_endpoint = "/tokens/xapp_token/"
endpoint = "/artists"

def get_token():
    resp = requests.post(BASE_URL + token_endpoint,
                  data={
                      "client_id": env["CLIENT_ID"],
                      "client_secret": env["CLIENT_SECRET"]
                  })
    if resp.ok:
        return resp.json().get("token")


def get_artist(id_: str, headers: dict):
    resp = requests.get(BASE_URL + endpoint + f"/{id_}", headers=headers)
    if resp.ok:
        return resp.json()


def construct_answer(artists):
    info = []
    for artist in artists:
        info.append({"name": artist["sortable_name"], "birthday": artist["birthday"]})
    return info


def main(keys):
    token = get_token()
    headers = {"X-Xapp-Token" : token}
    artists = []
    for key in keys:
        artists.append(get_artist(key.strip(), headers))

    return construct_answer(artists=artists)



if __name__ == "__main__":
    with open("dataset_24476_4.txt", "r") as inf:
        keys = inf.readlines()
        results = main(keys)
        results.sort(key=lambda x: (x["birthday"], x['name']))

        for result in results:
            print(result.get("name"))
