count_vowel=0
count_waste=0
count=0
count_consonant = 0
vowels=['a','e','i','o','u']

with open('source.txt', 'r') as fh:
    for line in fh:
        words = line.split()
        for i in words:
            for letter in i:
                count+=1
                if letter in vowels:
                    count_vowel+=1
                if (letter.isnumeric()):
                    count_waste+=1
                elif letter not in vowels:
                    count_consonant+=1
count_consonant = count_consonant - count_waste
print(count_vowel)
print(count_consonant)
print(count_waste)
print(count)