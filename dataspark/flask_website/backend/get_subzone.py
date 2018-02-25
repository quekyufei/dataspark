import os 

def get_subzone(subzone):
    subzone_dict = {}
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, "subzones.txt"), "r") as file:
        for line in file:
            (key, val) = line.split('\t')
            subzone_dict[key] = val.replace("\n", "")
    if subzone_dict[subzone]:
        return subzone_dict[subzone]
    else:
        return 'Null'

#print(get_subzone('GLSZ04'))




