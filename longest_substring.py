

def find_longest_sub_string(s):
    usedChar = {}
    start = maxLength = 0

    for i, char in enumerate(s):
        if char in usedChar and start <= usedChar[char]:
            start = usedChar[char] + 1
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[char] = i

    return maxLength

s = "bbbbbabc"
print(find_longest_sub_string(s))