def count_vowels(sentence):
    vowels = "aeiouAEIOU"
    vowelCounter = 0
    for char in sentence:
        if char in vowels:
            vowelCounter += 1
    return vowelCounter

sentence = input("Enter a sentence ")
print(count_vowels(sentence))