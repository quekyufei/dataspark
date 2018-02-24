
def get_subzone(subzone):
    subzone_dict = {}
    with open("subzones.txt", "r") as file:
        for line in file:
            (key, val) = line.split('\t')
            subzone_dict[key] = val.replace("\n", "")
    if subzone_dict[subzone]:
        return subzone_dict[subzone]
    else:
        return 'Null'

print(get_subzone('GLSZ04'))




