# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.

def counting_vowels_and_consonants(string):
    count_vowel = 0
    count_consonant = 0 #these are dummy variables representing the number of vowels or consonants
    for character in string:
        if character.isalpha() == True:
            if character in ['a', 'e', 'i', 'o', 'u', 'A','E','I','O','U']:
                count_vowel += 1
            else:
                count_consonant += 1
    return (count_vowel, count_consonant)

# print(counting_vowels_and_consonants("Fall in love with some activity, and do it! "))



# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

def average_vowels_and_consonants(paragraph):
    sentence_list = []
    for character in paragraph:    
        if character == '.' or character == '!':
            sentence_list.append(character)
    number_sentences = len(sentence_list)
    cvc = counting_vowels_and_consonants(paragraph) #cvc is an acronym for counting vowels and consonants
    av = cvc[0]/number_sentences
    ac = cvc[1]/number_sentences
    print(number_sentences, av, ac)




# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)

# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 
average_vowels_and_consonants(paragraph)
print(counting_vowels_and_consonants(paragraph))
# print(type(len(sentence_list)))