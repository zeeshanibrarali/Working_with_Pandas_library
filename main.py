import pandas

data = pandas.read_csv("./World_Happiness_2015.csv")
regions = data["Region"].tolist()
countries = data["Country"].tolist()
happiness = data["Happiness Rank"].tolist()

new_list = []
new_list_count = 0
E_list = []
E_list_count = 0
Se_list = []
Se_list_count = 0
S_list = []
S_list_count = 0

index = []
happyRank = []
max1 = 0
min1 = 158
# TODO: take out the asian region countries from the data.
for i in range(158):
    if "Asia" in regions[i]:
        if "Southeastern" in regions[i]:
            Se_list.append(countries[i])
            Se_list_count += 1
        if "Eastern" in regions[i]:
            E_list.append(countries[i])
            E_list_count += 1
        if "Southern" in regions[i]:
            S_list.append(countries[i])
            S_list_count += 1
        new_list.append(countries[i])
        happyRank.append(happiness[i])
        new_list_count += 1
        index.append(i)
        if happiness[i] > max1:
            max1 = happiness[i]
            max_c = countries[i]
        if min1 > happiness[i]:
            min1 = happiness[i]
            min_c = countries[i]

print("All asian countries ", new_list_count, " and names are : ")
print(new_list)

# TODO: then differentiate into further asian regions and show their count.
print("Southern asian countries", S_list_count, " and names are : ")
print(S_list)
print("SouthEastern asian countries", Se_list_count, " and names are : ")
print(Se_list)
print("Eastern asian countries", E_list_count, " and names are : ")
print(E_list)

# TODO: then show their happiness ratio among all asian countries.
print("\n")
print("The country with the lowest rank in Asia in Happiness Rank is : ", max_c)
print("The country with the highest rank in Asia in Happiness Rank is : ", min_c)




