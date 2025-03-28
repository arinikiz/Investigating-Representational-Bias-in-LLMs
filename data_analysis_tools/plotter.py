'''
This custom python script is used for determining the genders, ethnicities, sexual orientation that are mentioned in the filtered responses and their corresponding counts.
Then the relevant data is visualized using pyplot for better analysis.

'''

import matplotlib.pyplot as plt


def counter(dic):
  cntr = 0
  for i in dic.values():
    cntr += i
  if cntr != 200:
    print(f"count mismatch in {dic}\n total count: {cntr}")
  print("Success")

fstream = open("phase2_filtered.txt", mode="r")
lines = fstream.readlines()
fstream.close()

gender_count = {}
ethnicity_count = {}
sexor_count = {}

for line in lines:
  line = line.strip()
  if "Gender" in line:
    gender = line.split(":")[1].strip()
    if gender in gender_count:
      gender_count[gender] += 1
    else:
        gender_count[gender] = 1
  
  if "Ethnicity" in line:
    ethnicity = line.split(":")[1].strip()
    if ethnicity in ethnicity_count:
      ethnicity_count[ethnicity] += 1
    else:
        ethnicity_count[ethnicity] = 1

  if "Sexual Orientation" in line:
    sexor = line.split(":")[1].strip()
    if sexor in sexor_count:
      sexor_count[sexor] += 1
    else:
      sexor_count[sexor] = 1




#### Plotting ####


# Plotting the gender graph
xvals = list(gender_count.keys())
yvals = list(gender_count.values())

plt.bar(xvals,yvals, width=0.1,color="orange")
plt.xlabel("Gender")
plt.ylabel("Frequency")
plt.title("Frquency Distribution of Genders")
plt.grid(True, axis='y', alpha=0.5)
plt.xlim(-0.5, 0.5)
plt.show()


# Plotting the Ethnicity graph
plt.figure(figsize=(10,8))
xvals = list(ethnicity_count.keys())
yvals = list(ethnicity_count.values())
plt.bar(xvals,yvals)
plt.xlabel("Ethnicity")
plt.ylabel("Frequency")
plt.xticks(size="small",rotation=90)
plt.xlim(-1, 15)
plt.grid(True, axis="y", alpha=0.5)
plt.show()


