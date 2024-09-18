#Bob Klemm
#9/17/2024

#Magic Square of Squares Unsolved Problem

"""
for a in range(1,100):
    for b in range(2,100):
        for c in range(3,100):
            if (c-b)*(c+b) == (b-a)*(b+a) and a < b and b < c:
                #print(a**2, b**2, c**2) #arithmetic progression of squares
"""
x = 500
def magicsum():
    sum = []
    f = [[14, 1]]
    g = []
    for a in range(1,x):
        for b in range(a+1,x):
            for c in range(b+1,x):
                s = a**2+b**2+c**2
                sum.append(s)
    sum.sort()
    d = 14
    for i in sum:
        if i != d:
            f.append([i, 1])#count occurrences of sums
        else: 
            f[-1][1] += 1
            if f[-1][1] >= 6:
                #print(i) #is there a common sum that can be created 6 different ways?
                magicways(i)
                #print(str(f[-1][1]) + " unique ways.")
        d = i

def magicways(n):
    h = []
    h2 = [[0,0]]
    g = 0
    t = []
    for a in range(1,20):
        for b in range(a+1,20):
            for c in range(b+1,20):
                s = a**2+b**2+c**2
                if s == n:
                    t.append([a**2, b**2, c**2])
                    h.append(a**2)
                    h.append(b**2)
                    h.append(c**2)
    h.sort()
    d = 1
    for k in h:
        if k != d:
            h2.append([k, 1])#count occurrences of squares
        else: 
            h2[-1][1] += 1
            if h2[-1][1] == 3:
                g += 1
        d = k

    if g >= 1: #four corners of magic square needed
        print("The sum is " + str(n))
        print(str(g) + " triple points.") #triple point would be involved in three sums
        print(h2)
        print(t)
        
        
"""
r = [314, 329, 341, 374, 446]

for j in r:
    print(j)
    magicways(j)
"""



magicsum()