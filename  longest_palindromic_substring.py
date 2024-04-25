

def longest_palindromic(string_data):
    all_string = []
    sub_data = []
    temp = ''
    for i in string_data:
        if i not in sub_data:
            sub_data.append(i)
        else:
            temp += i
            sub_data.append(i)
            if ''.join(sub_data) == ''.join(sub_data)[::-1]:
                all_string.append(''.join(sub_data))
            sub_data.clear()
    if not all_string and temp+sub_data[0] == temp+sub_data[0][::-1]:
        return string_data
    return max(all_string) if all_string else ''.join(sub_data)[0] if sub_data else ''

s = "ac"
print(longest_palindromic(s))