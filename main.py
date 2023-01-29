vowels = ['a', 'e', 'i', 'o', 'u']
vowel_counter = 0
string = input('Enter a string')
for letter in string:
    if letter in vowels:
        vowel_counter += 1
print('Number of vowels:', vowel_counter)
