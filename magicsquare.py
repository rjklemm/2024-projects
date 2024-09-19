#Bob Klemm
#9/17/2024

#Magic Square of Squares Unsolved Problem

import math

def magicsum():
    sums = []
    sum_count = [[14, 1]] #initial occurrence of first sum (1+4+9)
    x = 500 #maximum tested value

    # a, b, and c are the integer square roots of the squares being summed.

    for a in range(1,x):
        for b in range(a+1,x):
            for c in range(b+1,x):
                sum = a**2+b**2+c**2
                sums.append(sum)
    sums.sort()
    last_sum = 14
    for value in sums:
        if value != last_sum:
            sum_count.append([value, 1])#unique sum count start at 1
        else: 
            sum_count[-1][1] += 1 #add count to same sum value
            if sum_count[-1][1] >= 6:
                #is there a common sum that can be created 6 different ways?
                magicways(value)
                #print(str(sum_count[-1][1]) + " unique ways.")
        last_sum = value

def magicways(common_sum):
    square_list = [] 
    square_list_2 = [[1,0]]
    corner_count = 0 
    middle_count = 0
    side_count = 0
    square_sum_list = [] #list of squares being summed together for a common sum
    x = math.ceil(math.sqrt(common_sum))# maximum tested value
    for a in range(1,x):
        for b in range(a+1,x):
            for c in range(b+1,x):
                sum = a**2+b**2+c**2
                if sum == common_sum:
                    square_sum_list.append([a**2, b**2, c**2])
                    square_list.append(a**2)
                    square_list.append(b**2)
                    square_list.append(c**2)
    square_list.sort()
    last_square = 1
    for new_square in square_list:
        if new_square != last_square:
            square_list_2.append([new_square, 1])#count occurrences of squares
        else: 
            square_list_2[-1][1] += 1
            if square_list_2[-1][1] == 2:
                side_count += 1
            if square_list_2[-1][1] == 3:
                corner_count += 1
            if square_list_2[-1][1] == 4:
                middle_count += 1
        last_square = new_square

    if middle_count >= 1 and corner_count >= 5 and side_count >= 9: #four corners of magic square needed, plus middle and sides
        print("The common sum is " + str(common_sum))
        print(str(side_count) + " double counts.")
        print(str(corner_count) + " triple counts.") #"triple count" would be involved in three sums, a possible corner
        print(str(middle_count) + " quadruple counts.")
        print(square_list_2)
        print(square_sum_list)
        
magicsum()