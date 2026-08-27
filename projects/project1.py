# Fake News Headline Projector 

# importing random module

import random

# create subjects list

subjects = [
    "Shahrukh Khan",
    "Samay Raina",
    "Modi",
    "Sourav Joshi",
    "A group of tiktokers",
    "Anime Fans",
    "Stary Dogs",
    "Heavy Rains",
    "Auto Rickshaw from Mumbai"
]

# creating actions 

actions = [
    "celebrates",
    "launches",
    "cancels the",
    "ate a heavy meal",
    "got robbed",
    "got allegations on",
    "backed out of the",
    "splitted out",
    "celebrates"
]

# creating objects

objects = [
    "At Red fort",
    "India's got latent",
    "During IPL Match",
    "At india gate",
    "Show",
    "At park",
    "Protest",
    "Ad",
    "at home",
    "at Bar"
]

while True :
    subject = random.choice(subjects)
    join = random.choice(actions)
    place = random.choice(objects)

    headline = f"BREAKING NEWS : {subject} {join} {place}"
    print(f"\n {headline}")

    user = input("\n Do you want to generate another headline (yes/no)").strip().lower()
    if user =="no":
        break

print("\n Thank you for using fake news headline generator")
