# Task #1.
# Описание Реализуйте функцию, определяющая, является ли одна строка перестановкой другой (полиндром). Под перестановкой понимаем любое изменение порядка символов. Регистр учитывается, пробелы являются существенными.

def isAnagram (str1, str2):                 # checks if one string consists the same sets of symbols as another string but in different order
    splitstr1 = [char for char in str1]     # whole set of symbols presented in string
    splitstr2 = [char for char in str2]     
    splitstr1.sort()                        # sorting set of symbols
    splitstr2.sort()                        
    return (
            str1!=str2 and                      # strings               should not be equal
            splitstr1==splitstr2                # srted sets of symbols should     be equal
            )

str1 = str(input('Enter first  string: '))   
str2 = str(input('Enter second string: '))
print('Are these strings consist same sets of symbols but in different order?')
print(isAnagram(str1, str2))