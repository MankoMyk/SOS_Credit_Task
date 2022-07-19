# Task #2.
# Описание Реализуйте функцию сжатия строки на основе счетчика повторяющихся символов. Например, строка aabcccccaaa должна превратиться в а2b1с5аЗ. Если «сжатая» строка оказывается длиннее исходной, метод должен вернуть исходную строку. 

def compressString(string):
    result = ""
    count = 1
    for i in range(1, len(string)):
        if string[i-1] == string[i]:
            count += 1
        else:
            result += string[i-1]
            result += str(count)    # put condition "if count > 1" to avoid counting 1 symbol
            count = 1
    result += string[-1]
    result += str(count)            # put condition "if count > 1" to avoid counting 1 symbol
    if len(result)>len(string):     # if compressed string is longer, - keep the origin string
        result = string
    return result

string = str(input('Enter the string to be compressed: '))   
res = compressString(string)
if res == string:
    print('Compressed string is longer than entered string, so the origin one was kept: ')
else:
    print('Compressing is successful, here is the result: ')
print(res)