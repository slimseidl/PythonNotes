filename = input()

cats = []
name = []
desc = []
availability = []

with open(filename, 'r') as foodfile:
    for line in foodfile:
        parts = line.strip().split('\t')
        
        cats.append(parts[0])
        name.append(parts[1])
        desc.append(parts[2])
        availability.append(parts[3])
    
for i in range(len(availability)):
    if availability[i] == "Available":
        print(f'{name[i]} ({cats[i]}) -- {desc[i]}')