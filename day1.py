# Advent of Code
# Day 1

# Get input
def process_input():
    clean = []
    with open('input-day1.txt') as f:
        input = f.readlines()
    for i in input:
        clean.append(int(i.strip()))
    return(clean)

def day1_1(input):
    previous, count = 0, 0
    for i in input:
        if previous == 0:
            previous = i
        elif i > previous:
            count+=1
            previous = i
        else:
            previous = i
    print(f"Day 1 - Part 1 answer is: {count}")

def day1_2(input):
    count = 0
    for i in range(0,len(input)):
        first = (input[i:i+3])
        second = (input[i+1:i+4])
        if len(first) & len(second) ==3:
            if(sum(second)>sum(first)):
                count+=1
    print(f"Day 1 - Part 2 answer is: {count}")

day1_input = process_input()
day1_1(day1_input)
day1_2(day1_input)

