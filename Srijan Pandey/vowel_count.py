# WRITE A PROGRAM FOR COUNTING NUMBER OF VOWEL LETTERS.

while True:
    sentence=input(str("Enter the word/sentence: "))
    vowels=("aeiouAEIOU")
    vowel_count=0
    for letters in sentence:
        if letters in vowels:
            vowel_count+=1
    print(vowel_count)