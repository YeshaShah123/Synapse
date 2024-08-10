from itertools import combinations

Kevin = {"Halsey", "Taylor Swift", "Mitski", "Joji", "Shawn Mendes", "Sabrina Carpenter", "Nicky Minaj", "Conan Gray", "One Direction", "Justin Bieber"}
Stuart = {"Kendrick Lamar", "Steve Lacy", "Tyler the Creator", "Joji", "TheWeeknd", "Coldplay", "Kanye West", "Travis Scott", "Frank Ocean", "Brent Faiyaz"}
Bob = {"Conan Gray", "Joji", "Dove Cameron", "Mitski", "Arctic Monkeys", "Steve Lacy", "Kendrick Lamar", "Isabel LaRosa", "Shawn Mendes", "Coldplay"}
Edith ={"Metallica", "Billie Eilish", "TheWeeknd", "Mitski", "NF", "Conan Gray", "Kendrick Lamar", "Nicky Minaj", "Kanye West", "Coldplay"}



DJ= {"Kevin":Kevin ,"Stuart":Stuart, "Bob":Bob, "Edith":Edith}
combs = list(combinations(DJ.keys(), 2))

print(combs) 

#[('Kevin', 'Stuart'), ('Kevin', 'Bob'), ('Kevin', 'Edith'), ('Stuart', 'Bob'), ('Stuart', 'Edith'), ('Bob', 'Edith')] - Output

def calculate_overlap(set1, set2):
    intersection = len(set1.intersection(set2))
    return intersection / len(set1), intersection / len(set2)

set=[]

for dj1, dj2 in combs:
    overlap1, overlap2 = calculate_overlap(DJ[dj1], DJ[dj2])
    if overlap1 >= 0.3 and overlap2 >= 0.3:
        avg_overlap = (overlap1 + overlap2) / 2 
        set.append(((dj1, dj2), avg_overlap, overlap1, overlap2))

set.sort(key=lambda x: x[1], reverse=True)

for pair in set:
    print(f"{pair[0][0]} & {pair[0][1]}: {pair[1]*100}% overlap" )

#Kevin & Bob: 40.0% overlap
#Stuart & Bob: 40.0% overlap
#Stuart & Edith: 40.0% overlap
#Bob & Edith: 40.0% overlap
#Kevin & Edith: 30.0% overlap
 


