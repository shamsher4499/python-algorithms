def check_balance_brackets(string_data):
    bracket_dict = {'{':0, '}':0, '(':0, ')':0, '[':0, ']':0}
    for char in string_data:
        if char in bracket_dict:
            bracket_dict[char] += 1

    return bracket_dict['{'] == bracket_dict['}'] and bracket_dict['('] == bracket_dict[')'] and bracket_dict['['] == bracket_dict[']']

print(check_balance_brackets('](){}[[[]]][)'))