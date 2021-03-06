import csv
from datetime import datetime
from pprint import pprint

def convert2ampm(time24: str):
    return datetime.strptime(time24, "%H:%M").strftime("%I:%M%p")

with open("buzzers.csv") as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(",")
        flights[k] = v

pprint(flights)

flights2 = {}

for k, v in flights.items():
    flights2[convert2ampm(k)] = v.title()

pprint(flights2)

dest = set(flights2.values())

when = {thing: [k for k, v in flights2.items() if v == thing]
        for thing in dest}
