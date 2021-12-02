# Advent of Code
# Day 1
# Part 1
clean = []
with open('input-day1.txt') as f:
    input = f.readlines()

for i in input:
    clean.append(int(i.strip()))
previous, count = 0, 0

for i in clean:
    if previous == 0:
        previous = i
    elif i > previous:
        count+=1
        previous = i
    else:
        previous = i
print(f"Day 1 - Part 1 answer is: {count}")


# Day 1
# Part 2
count = 0

for i in range(0,len(clean)):
    first = (clean[i:i+3])
    second = (clean[i+1:i+4])
    if len(first) & len(second) ==3:
        if(sum(second)>sum(first)):
            count+=1

print(f"Day 1 - Part 2 answer is: {count}")


