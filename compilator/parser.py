import compilator.build_in as build_in

def parse(source):
    if type(source) is not list or source == []:
        return

    for i in source:
        restructured_space = i.split()
        print(i, restructured_space)
        # DEFINITION FUNCTIONS OR VARIABLES
        if i[0] == "." and restructured_space[0][1:] in build_in.functions and len(restructured_space) == 2:
            print(restructured_space[1])
