'''
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''


def roman_to_integer(s) -> int:
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    integer = 0
    prev = 0
    for i in range(len(s)):
        if roman_dict[s[i]] > prev:
            integer += roman_dict[s[i]] - 2 * prev
        else:
            integer += roman_dict[s[i]]
        prev = roman_dict[s[i]]
    return integer

roman_val = 'IX'
print(roman_to_integer(roman_val)) # 1994