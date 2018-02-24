subzoneDict = {}
with open("subzones.txt", "r") as file:
    for line in file:
        (key, val) = line.split('\t')
        subzoneDict[key] = val.replace("\n", "")

for i in subzoneDict:
    print(i + "\t" + subzoneDict[i])

