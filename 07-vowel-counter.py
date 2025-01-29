
vowels = ['a', 'e', 'i', 'o', 'u']

def count_of_vowels(word):
    quantity=0
    for letter in word:
        if( letter in vowels ):
            quantity += 1
    
    return quantity

result = count_of_vowels('Hola Mundo')
print(result)