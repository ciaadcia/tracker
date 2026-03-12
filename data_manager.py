import json
import os

FILE = "data.json"


def load_data():
    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_points(name, points):

    data = load_data()

    if name not in data:
        data[name] = 0

    data[name] += points

    save_data(data)

    return data[name]