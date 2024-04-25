'''
input='Hello World'
output=5

input=' Fly high in the  sky _  '
output=3
'''


def word_count(str):
    char_data = str.split(' ')
    char_data = [item for item in char_data if item not in ['', '_']]
    return len(char_data[-1])

input='Hello World'
print(word_count(input))