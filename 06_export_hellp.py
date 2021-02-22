import os

copper = []

for cu in os.listdir("Mystery_box_winnings_images/cu"):
    if cu.endswith(".gif"):
        copper.append("Mystery_box_winnings_images/cu/{}".format(cu))

copper.sort()
print(copper)

silver = []
for ag in os.listdir("Mystery_box_winnings_images/ag"):
    if ag.endswith(".gif"):
        silver.append("Mystery_box_winnings_images/ag/{}".format(ag))

silver.sort()
print(silver)

gold = []
for au in os.listdir("Mystery_box_winnings_images/au"):
    if au.endswith(".gif"):
        gold.append("Mystery_box_winnings_images/au/{}".format(au))

gold.sort()
print(gold)