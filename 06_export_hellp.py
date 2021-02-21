import os

copper = []
for cu in os.listdir("Mystery_box_winnings_images/cu"):
    if cu.endswith(".gif"):
        copper.append(cu)

print(copper)


silver = []
for ag in os.listdir("Mystery_box_winnings_images/ag"):
    if ag.endswith(".gif"):
        silver.append(ag)

print(silver)

gold = []
for au in os.listdir("Mystery_box_winnings_images/au"):
    if au.endswith(".gif"):
        gold.append(au)

print(gold)

