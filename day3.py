# Advent of Code
# Day 3

# Import functions
from commonfunctions import process_input

def day3_1(input):
    gamma = ""
    epsilon = ""
    for x in range(len(input[0])):
        count = 0
        for i in input:
            if i[x] == str(1):
                count += 1
        if count > len(input)/2:
            gamma += '1'
        else:
            gamma += '0'

    for x in range(len(gamma)):
        if gamma[x] == str(1):
            epsilon += '0'
        else:
            epsilon += '1'
    print(f"Day 2 - Part 1 answer is: {int(epsilon,2)*int(gamma,2)}")
    
def day3_2(input):
    print(input)
    print(day3_2_oxygen(input))
    
    


def day3_2_oxygen(input, count=None):
    oxygen = []
    if count == None:
        count = 0
    if len(input) >1:
        if sum([int(i[count]) for i in input]) < len(input)/2:
            input = remove_values(input,count,1)
        else:
            input = remove_values(input,count,0)
        count +=1
        day3_2_oxygen(input,count)
    elif len(input) == 1:
        #return(input[0])
        return(1)
        
    
        
        
    
def remove_values(input,position,value):
    values = []
    for i in input:
        if i[position] != str(value):
            values.append(i)
    return(values)
           
        
file = 'input-day3.txt'
#input = process_input(file)
input=['00100','11110','10110','10111','10101','01111','00111','11100','10000','11001','00010','01010']

#day3_1(input)
day3_2(input)
