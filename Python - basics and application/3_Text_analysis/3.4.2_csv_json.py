import json
from pathlib import Path
from typing import List

BASE_DIR = Path("__file__").resolve().parent.parent
FILENAME = Path.joinpath(BASE_DIR, "./test.json")

with open(FILENAME, "r") as inf:
    data = json.load(inf)


def count_parents(parents: List[dict], counter_: dict=None) -> dict:
    if counter_ is None:
        counter_ = {parent["name"]: 1 for parent in parents}

    if isinstance(parents, list):
        for parent in parents:
            if isinstance(parent, dict):
                count_parents(parent["parents"], counter_)
            else:
                if parent in counter_:
                    counter_[parent] += 1
                else:
                    counter_[parent] = 1
        return counter_


res = count_parents(data)
keys_= sorted(res.keys())
sorted_res = {key_: res[key_] for key_ in keys_}
for k, v in sorted_res.items():
    print(f"{k} : {v}")