import sys

def main():
    path = [(0,0),]
    x, y = 0, 0
    crossed = 0
    curpos = (x, y)
    obs_file = input("Please give the name of the obstacles"\
        +" filename, or - for none:\n")
    obstacles = []
    if obs_file != "-" :
        obs_file.strip()
        obs_file = open(obs_file, 'r')
        for line in obs_file :
            if '#' not in line[0]:
                line = line.strip()
                if len(line.split()) == 0:
                    continue
                line = line.split()
                try:
                    o_x = int(line[0])
                    o_y = int(line[1])
                    obstacles.append((o_x,o_y))
                except: 
                    "ERROR - error reading line in file."
                    continue
    print("Current position:\t" + str(path[-1]))
    print("Your history:\t\t" + str(path[0:]))
    print("What is your next command?")
    for line in sys.stdin :
        try:
            command = line.strip()
        except IOError :
            print("ERROR - invalid input")
            continue
        curpos = path[-1]
        if len(command) == 0 :
            print("You do nothing.")
        elif command == "n" :
            y += 1
            curpos = (x, y)
            if curpos not in obstacles :
                path.append(curpos)
        elif command == "e" :
            x += 1
            curpos = (x, y)
            if curpos not in obstacles :
                path.append(curpos)
        elif command == "s" :
            y -= 1
            curpos = (x, y)
            if curpos not in obstacles :
                path.append(curpos)
        elif command == "w" :
            x -= 1
            curpos = (x, y)
            if curpos not in obstacles :
                path.append(curpos)
        elif command == "back" :
            if len(path) == 1:
                print("Cannot move back, as you're at the start!")
                print()
                print("Current position:\t" + str(path[-1]))
                print("Your history:\t\t" + str(path[0:]))
                print("What is your next command?")
                continue
            path.pop()
            curpos = path[-1]
            print("You retrace your steps by one space")
        elif command == "crossings" :
            curpos = path[-1]
            for i in path :
                if curpos == i :
                    crossed += 1
            print ("There have been " + str(crossed) + \
                " times in the history when you were at this point.")
            crossed = 0
        elif command == "ranges" :
            maxwest, maxeast, maxsouth, maxnorth = 0, 0, 0, 0
            for i in path :
                if int(i[0]) < maxwest :
                    maxwest = int(i[0])
                if int(i[0]) > maxeast :
                    maxeast = int(i[0])
                if int(i[1]) < maxsouth :
                    maxsouth = int(i[1])
                if int(i[1]) > maxnorth :
                    maxnorth = int(i[1])
            print("The furthest West you have ever walked is " + str(maxwest))
            print("The furthest East you have ever walked is " + str(maxeast))
            print("The furthest South you have ever walked is " + str(maxsouth))
            print("The furthest North you have ever walked is " + str(maxnorth))
        elif command == "map" :
            maxwest, maxeast, maxsouth, maxnorth = 0, 0, 0, 0
            for i in path :
                if int(i[0]) < maxwest :
                    maxwest = i[0]
                if int(i[0]) > maxeast :
                    maxeast = i[0]
                if int(i[1]) < maxsouth :
                    maxsouth = i[1]
                if int(i[1]) > maxnorth :
                    maxnorth = i[1]
            a, b = maxnorth, maxwest
            while a >= maxsouth :
                b = maxwest
                while b <= maxeast :
                    if (b,a) == path[-1] :
                        print("+", end="")
                    elif (b,a) == (0,0) :
                        print("*", end="")
                    elif (b,a) in path :
                        print("X", end="")
                    elif (b,a) in obstacles:
                        print(" ", end="")
                    else :
                        print(".", end="")
                    b += 1
                a -= 1
                print()
        else :
            print("ERROR - Invalid command: " + command)
        print()
        print("Current position:\t" + str(path[-1]))
        print("Your history:\t\t" + str(path[0:]))
        print("What is your next command?")
    
if __name__ == "__main__":
    main()