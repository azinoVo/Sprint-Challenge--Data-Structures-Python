import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# so total complexity is about 0(n^2) which is pretty huge since n is 10,000
# For each of the 10,000, it has to iterate over each of the other 10,000 so 10,000^2

# duplicates = []
# for name_1 in names_1: # O(n)
#     for name_2 in names_2: # O(n)
#         if name_1 == name_2: # O(1)
#             duplicates.append(name_1) O(1)

# Python seems to have a bunch of methods for comparing two sets of data, returning differences and similarities
# Can I use this?

# duplicates = names_1.intersection(names_2)
duplicates = list(set(names_1) & set(names_2))
print("SET?", duplicates)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

