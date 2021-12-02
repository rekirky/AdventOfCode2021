# Advent of Code
# Day 2

# Get input
def process_input(file):
    clean = []
    with open(file) as f:
        input = f.readlines()
    for i in input:
        clean.append(i.strip())
    return(clean)

def day2_1(input):
    xpos,ypos = 0,0
    for i in input:
        direction = i.split()
        if direction[0] == "forward": xpos += int(direction[1])
        elif direction[0] == "up": ypos -= int(direction[1])
        elif direction[0] == "down": ypos += int(direction[1])
    print(f"Day 2 - Part 1 answer is: {xpos*ypos}")
    
def day2_2(input):
    xpos,ypos,aim = 0,0,0
    for i in input:
        direction = i.split()
        if direction[0] == "forward":
            xpos += int(direction[1])
            ypos += (aim*int(direction[1]))
        elif direction[0] == "up": aim -= int(direction[1])
        elif direction[0] == "down": aim += int(direction[1])
    print(f"Day 2 - Part 2 answer is: {xpos*ypos}")

file = "input-day2.txt"
input = process_input(file)    
day2_1(input)
day2_2(input)


