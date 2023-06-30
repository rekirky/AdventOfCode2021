# Advent of Code
# Day 4

<<<<<<< Updated upstream
# Import functions
import numpy as np
from commonfunctions import process_input


def bingo_numbers(input):
    print(1)


file = "input-day4(test).txt"
#file = "input-day4.txt"

clean = []
with open(file) as f:
    bingo = f.readline()
    input = f.readlines()
    for i in input:
        clean.append(i.strip())


print(bingo)
print(clean)    

letter = 68
fix = []
for i in clean[1:6]:
    fix.append(i.split())

def day3_2(input):    
    for i in range(len(fix)):
        for x in range(len(fix[i])):
            if int(fix[i][x]) == letter:
                print("hit")
                fix[i][x] = -1


print(clean)

def check_str_line(input):
    for i in range(len(input)):
        check = 0
        for x in range(len(input[i])):
            check += int(input[i][x])
        if check == -5:
            print("Line hit")
        
def check_str_col(input):
    for i in range(5):
        check = 0
        for x in range(5):
            check += int(input[x][i])
        if check == -5:
            print("Col Hit")
        

#check_str_col(input)
#check_str_line(clean)





letter = 68


#boards = np.full((5,5),clean[1:6])


#print(boards)





=======
def process_input(file):
    clean = []
    with open(file) as f:
        input = f.readlines()
    for i in input:
        clean.append(i.strip())
    return(clean)

def card_generator(bingo_cards,bingo_numbers):
    for i in range(0,round(len(bingo_cards)),6):
        card = bingo_cards[i:i+5]
        card = card_checker(card,bingo_numbers)
                
        
        
def card_checker(card,bingo_numbers):
    updated_card = []
    for i in bingo_numbers:
        check = i
        for x in card:
            card = list(map(int,x.split()))
            for y in card:
                if int(y) == check:
                    updated_card.append(-1)
                else:
                    updated_card.append(y)
        print(card)
        print(updated_card)
        
                    


file = "input-day4test.txt"
#file = "input-day4.txt"
input = process_input(file)
bingo_numbers = list(map(int,input[0].split(",")))
bingo_cards = input[2:]

card_generator(bingo_cards,bingo_numbers)


#for i in bingo_numbers:
 #   card_generator(i)
>>>>>>> Stashed changes
