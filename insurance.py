#Bob Klemm
#6/12/2024

# Codecademy Medical Insurance Project

#open file
file = open("insurance.csv")
#print(file.read())

#organizing the data
data = []

age = []
sex = []
bmi = []
children = []
smoker = []
region = []
charges = []

num = 0
for line in file:
    linelist = line.split(',')
    if num > 0:
        linelist[0] = int(linelist[0])
        age.append(linelist[0])
        sex.append(linelist[1])
        linelist[2] = float(linelist[2])
        bmi.append(linelist[2])
        linelist[3] = int(linelist[3])
        children.append(linelist[3])
        smoker.append(linelist[4])
        region.append(linelist[5])
        linelist[6].replace('\n','0')
        linelist[6] = float(linelist[6])
        charges.append(linelist[6])
        num += 1
        data.append(linelist)
    num += 1


"""    
print(data)
print(age)
print(sex)
print(bmi)
print(children)
print(smoker)
print(region)
print(charges)
"""

#analyze the data

#age 
age_dist = [0,0,0,0,0,0,0,0]

for num0 in age:
    if num0 < 20:
        age_dist[0] += 1
    elif num0 >= 20 and num0 < 30:
        age_dist[1] += 1
    elif num0 >= 30 and num0 < 40:
        age_dist[2] += 1
    elif num0 >= 40 and num0 < 50:
        age_dist[3] += 1
    elif num0 >= 50 and num0 < 60:
        age_dist[4] += 1
    elif num0 >= 60 and num0 < 70:
        age_dist[5] += 1
    elif num0 >= 70 and num0 < 80:
        age_dist[6] += 1
    else:
        age_dist[7] += 1

print(str(age_dist[0]) + " teens were surveyed.")
print(str(age_dist[1]) + " 20-somethings were surveyed.")
print(str(age_dist[2]) + " 30-somethings were surveyed.")
print(str(age_dist[3]) + " 40-somethings were surveyed.")
print(str(age_dist[4]) + " 50-somethings were surveyed.")
print(str(age_dist[5]) + " 60-somethings were surveyed.")

#sex
sex_dist = [0,0]

for sex0 in sex:
    if sex0 == "male":
        sex_dist[0] += 1
    elif sex0 == "female":
        sex_dist[1] += 1
    
print(str(sex_dist[0]) + " males were surveyed.")
print(str(sex_dist[1]) + " females were surveyed.")

#bmi

bmi_dist = [0,0,0,0,0,0,0,0]

for bmi0 in bmi:
    if bmi0 < 10:
        bmi_dist[0] += 1
    elif bmi0 < 15:
        bmi_dist[1] += 1
    elif bmi0 < 20:
        bmi_dist[2] += 1
    elif bmi0 < 25:
        bmi_dist[3] += 1
    elif bmi0 < 30:
        bmi_dist[4] += 1
    elif bmi0 < 35:
        bmi_dist[5] += 1
    elif bmi0 < 40:
        bmi_dist[6] += 1
    else:
        bmi_dist[7] += 1

print(str(bmi_dist[0]) + " people surveyed had a BMI less than 10.")
print(str(bmi_dist[1]) + " people surveyed had a BMI between 10 and 15.")
print(str(bmi_dist[2]) + " people surveyed had a BMI between 15 and 20.")
print(str(bmi_dist[3]) + " people surveyed had a BMI between 20 and 25.")
print(str(bmi_dist[4]) + " people surveyed had a BMI between 25 and 30.")
print(str(bmi_dist[5]) + " people surveyed had a BMI between 30 and 35.")
print(str(bmi_dist[6]) + " people surveyed had a BMI between 35 and 40.")
print(str(bmi_dist[7]) + " people surveyed had a BMI greater than 40.")


#children

children_dist = [0,0,0,0,0,0,0,0]

for children0 in children:
    if children0 == 0:
        children_dist[0] += 1
    elif children0 == 1:
        children_dist[1] += 1
    elif children0 == 2:
        children_dist[2] += 1
    elif children0 == 3:
        children_dist[3] += 1
    elif children0 == 4:
        children_dist[4] += 1
    elif children0 == 5:
        children_dist[5] += 1
    elif children0 == 6:
        children_dist[6] += 1
    else:
        children_dist[7] += 1

print(str(children_dist[0]) + " people surveyed had no children.")
print(str(children_dist[1]) + " people surveyed had one child.")
print(str(children_dist[2]) + " people surveyed had two children.")
print(str(children_dist[3]) + " people surveyed had three children.")
print(str(children_dist[4]) + " people surveyed had four children.")
print(str(children_dist[5]) + " people surveyed had five children.")
print(str(children_dist[6]) + " people surveyed had six children.")
print(str(children_dist[7]) + " people surveyed had more than six children.")


#smoker
smoker_dist = [0,0]

for smoker0 in smoker:
    if smoker0 == "no":
        smoker_dist[0] += 1
    elif smoker0 == "yes":
        smoker_dist[1] += 1
    
print(str(smoker_dist[0]) + " surveyed were non-smokers.")
print(str(smoker_dist[1]) + " surveyed were smokers.")


#region

region_dist = [0,0,0,0,0]

for region0 in region:
    if region0 == "northwest":
        region_dist[0] += 1
    elif region0 == "northeast":
        region_dist[1] += 1
    elif region0 == "southwest":
        region_dist[2] += 1
    elif region0 == "southeast":
        region_dist[3] += 1
    else:
        region_dist[4] += 1

print(str(region_dist[0]) + " surveyed lived in the northwest.")
print(str(region_dist[1]) + " surveyed lived in the northeast.")
print(str(region_dist[2]) + " surveyed lived in the southwest.")
print(str(region_dist[3]) + " surveyed lived in the southeast.")


#charges

charges_dist = [0,0,0,0,0,0]

for charges0 in charges:
    if charges0 < 5000:
        charges_dist[0] += 1
    elif charges0 < 10000:
        charges_dist[1] += 1
    elif charges0 < 15000:
        charges_dist[2] += 1
    elif charges0 < 20000:
        charges_dist[3] += 1
    elif charges0 < 25000:
        charges_dist[4] += 1
    else:
        charges_dist[5] += 1

print(str(charges_dist[0]) + " surveyed were charged less than $5000.")
print(str(charges_dist[1]) + " surveyed were charged between $5000 and $10000.")
print(str(charges_dist[2]) + " surveyed were charged between $10000 and $15000.")
print(str(charges_dist[3]) + " surveyed were charged between $15000 and $20000.")
print(str(charges_dist[4]) + " surveyed were charged between $20000 and $25000.")
print(str(charges_dist[5]) + " surveyed were charged over $25000.")


#in-depth analysis (BMI vs. other variables (smoker and region))

#BMI vs smoker

bmi_smoker_dist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(bmi)):
    if bmi[i] < 15 and smoker[i] == "no":
        bmi_smoker_dist[0] += 1
    elif bmi[i] < 15 and smoker[i] == "yes":
        bmi_smoker_dist[1] += 1
    elif bmi[i] < 20 and smoker[i] == "no":
        bmi_smoker_dist[2] += 1
    elif bmi[i] < 20 and smoker[i] == "yes":
        bmi_smoker_dist[3] += 1
    elif bmi[i] < 25 and smoker[i] == "no":
        bmi_smoker_dist[4] += 1
    elif bmi[i] < 25 and smoker[i] == "yes":
        bmi_smoker_dist[5] += 1
    elif bmi[i] < 30 and smoker[i] == "no":
        bmi_smoker_dist[6] += 1
    elif bmi[i] < 30 and smoker[i] == "yes":
        bmi_smoker_dist[7] += 1
    elif bmi[i] < 35 and smoker[i] == "no":
        bmi_smoker_dist[8] += 1
    elif bmi[i] < 35 and smoker[i] == "yes":
        bmi_smoker_dist[9] += 1
    elif bmi[i] < 40 and smoker[i] == "no":
        bmi_smoker_dist[10] += 1
    elif bmi[i] < 40 and smoker[i] == "yes":
        bmi_smoker_dist[11] += 1
    elif bmi[i] >= 40 and smoker[i] == "no":
        bmi_smoker_dist[12] += 1
    elif bmi[i] >= 40 and smoker[i] == "yes":
        bmi_smoker_dist[13] += 1

print(str(bmi_smoker_dist[0]) + " surveyed had a BMI less than 15 and were not a smoker.")
print(str(bmi_smoker_dist[1]) + " surveyed had a BMI less than 15 and were a smoker.")
print(str(bmi_smoker_dist[2]) + " surveyed had a BMI between 15 and 20 and were not a smoker.")
print(str(bmi_smoker_dist[3]) + " surveyed had a BMI between 15 and 20 and were a smoker.")
print(str(bmi_smoker_dist[4]) + " surveyed had a BMI between 20 and 25 and were not a smoker.")
print(str(bmi_smoker_dist[5]) + " surveyed had a BMI between 20 and 25 and were a smoker.")
print(str(bmi_smoker_dist[6]) + " surveyed had a BMI between 25 and 30 and were not a smoker.")
print(str(bmi_smoker_dist[7]) + " surveyed had a BMI between 25 and 30 and were a smoker.")
print(str(bmi_smoker_dist[8]) + " surveyed had a BMI between 30 and 35 and were not a smoker.")
print(str(bmi_smoker_dist[9]) + " surveyed had a BMI between 30 and 35 and were a smoker.")
print(str(bmi_smoker_dist[10]) + " surveyed had a BMI between 35 and 40 and were not a smoker.")
print(str(bmi_smoker_dist[11]) + " surveyed had a BMI between 35 and 40 and were a smoker.")
print(str(bmi_smoker_dist[12]) + " surveyed had a BMI greater than 40 and were not a smoker.")
print(str(bmi_smoker_dist[13]) + " surveyed had a BMI greater than 40 and were a smoker.")


#BMI vs region

bmi_region_dist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in range(len(bmi)):
    if bmi[i] < 20 and region[i] == "northwest":
        bmi_region_dist[0] += 1
    elif bmi[i] < 30 and region[i] == "northwest":
        bmi_region_dist[1] += 1
    elif bmi[i] < 40 and region[i] == "northwest":
        bmi_region_dist[2] += 1
    elif bmi[i] >= 40 and region[i] == "northwest":
        bmi_region_dist[3] += 1
    elif bmi[i] < 20 and region[i] == "northeast":
        bmi_region_dist[4] += 1
    elif bmi[i] < 30 and region[i] == "northeast":
        bmi_region_dist[5] += 1
    elif bmi[i] < 40 and region[i] == "northeast":
        bmi_region_dist[6] += 1
    elif bmi[i] >= 40 and region[i] == "northeast":
        bmi_region_dist[7] += 1
    elif bmi[i] < 20 and region[i] == "southwest":
        bmi_region_dist[8] += 1
    elif bmi[i] < 30 and region[i] == "southwest":
        bmi_region_dist[9] += 1
    elif bmi[i] < 40 and region[i] == "southwest":
        bmi_region_dist[10] += 1
    elif bmi[i] >= 40 and region[i] == "southwest":
        bmi_region_dist[11] += 1
    elif bmi[i] < 20 and region[i] == "southeast":
        bmi_region_dist[12] += 1
    elif bmi[i] < 30 and region[i] == "southeast":
        bmi_region_dist[13] += 1
    elif bmi[i] < 40 and region[i] == "southeast":
        bmi_region_dist[14] += 1
    elif bmi[i] >= 40 and region[i] == "southeast":
        bmi_region_dist[15] += 1
    

print(str(bmi_region_dist[0]) + " surveyed had a BMI less than 20 and lived in the northwest.")
print(str(bmi_region_dist[1]) + " surveyed had a BMI between 20 and 30 and lived in the northwest.")
print(str(bmi_region_dist[2]) + " surveyed had a BMI between 30 and 40 and lived in the northwest.")
print(str(bmi_region_dist[3]) + " surveyed had a BMI greater than 40 and lived in the northwest.")
print(str(bmi_region_dist[4]) + " surveyed had a BMI less than 20 and lived in the northeast.")
print(str(bmi_region_dist[5]) + " surveyed had a BMI between 20 and 30 and lived in the northeast.")
print(str(bmi_region_dist[6]) + " surveyed had a BMI between 30 and 40 and lived in the northeast.")
print(str(bmi_region_dist[7]) + " surveyed had a BMI greater than 40 and lived in the northeast.")
print(str(bmi_region_dist[8]) + " surveyed had a BMI less than 20 and lived in the southwest.")
print(str(bmi_region_dist[9]) + " surveyed had a BMI between 20 and 30 and lived in the southwest.")
print(str(bmi_region_dist[10]) + " surveyed had a BMI between 30 and 40 and lived in the southwest.")
print(str(bmi_region_dist[11]) + " surveyed had a BMI greater than 40 and lived in the southwest.")
print(str(bmi_region_dist[12]) + " surveyed had a BMI less than 20 and lived in the southeast.")
print(str(bmi_region_dist[13]) + " surveyed had a BMI between 20 and 30 and lived in the southeast.")
print(str(bmi_region_dist[14]) + " surveyed had a BMI between 30 and 40 and lived in the southeast.")
print(str(bmi_region_dist[15]) + " surveyed had a BMI greater than 40 and lived in the southeast.")