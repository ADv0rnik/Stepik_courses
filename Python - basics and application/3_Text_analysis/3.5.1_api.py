import requests
from pathlib import Path

BASE_DIR = Path("__file__").resolve().parent.parent
IN_FILE = Path.joinpath(BASE_DIR, "./work_files/dataset_24476_3.txt")
OUT_FILE = Path.joinpath(BASE_DIR, "./test_out.txt")

def send_request(num):
    BASE_URL = f"http://numbersapi.com/{num}/math?json=true"
    resp = requests.get(BASE_URL)
    results = resp.json()
    if results["found"]:
        return "Interesting"
    return "Boring"

with open(IN_FILE, "r") as inf:
    data = inf.readlines()
    nums = [int(dat.strip()) for dat in data]

with open(OUT_FILE, "w") as outf:
    for num in nums:
        res = send_request(num)
        outf.write(res + "\n")
    else:
        print("Done!")