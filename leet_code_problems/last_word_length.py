'''
Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

'''

def find_last_word_length(s:str) -> int:
    sep_words = s.split(" ")
    all_words = [i for i in sep_words if i not in ["",'']]
    return len(all_words[-1])

s = "luffy is still joyboy"
print(find_last_word_length(s))