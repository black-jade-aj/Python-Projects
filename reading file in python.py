colldata = {}  # empty dictionary

with open("colldata.txt", "r") as fh:
    line = fh.readlines()[0].strip()  # read the first line and strip newline characters
    presdata = line.split(",")   # split on commas into a list

colldata['lastname'] = presdata[0]
colldata['firstname'] = presdata[1]
colldata['height'] = presdata[2]
colldata['weight'] = presdata[3]

print(colldata)

all_people = []

with open("colldata.txt", "r") as fh:
    for line in fh:
        presdata = line.strip().split(",")
        if len(presdata) >= 4:
            person = {
                'lastname': presdata[0],
                'firstname': presdata[1],
                'height': presdata[2],
                'weight': presdata[3]
            }
            all_people.append(person)

print(all_people)