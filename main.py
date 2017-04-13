gift_code = ''

# ---------- # ---------- #

import random
import sys
import os

word_list = []
counter_list = []

app_path = os.path.dirname(os.path.abspath(sys.argv[0]))
file_path = os.path.join(app_path, 'word_list.txt')

with open(file_path, 'r') as fp:
    for line in fp:
        line = line.replace('\n', '')
        word_list.append(line)

out_string = ''
identifier_string = ''

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def insert_num(string, index, number):
    if index > 9:
        return string[:index] + str(number) + string[index:]
    else:
        return string[:index] + str(number) + string[index:]

counter = 1
for digit in gift_code:
    identifier_string += '      '
    random.shuffle(word_list)

    for word in word_list:
        if digit.lower() in word.lower():
            index = word.lower().find(digit.lower())
            if word[index].isupper():
                out_string += '\n' + f'{counter}. ' + word.replace(digit, '_', 1)
            else:
                out_string += '\n' + f'{counter}. ' + word.replace(digit.lower(), '_', 1)

            gift_code = gift_code.replace(digit, '_', 1)

            counter += 1
            break

while '__' in gift_code:
    gift_code = gift_code.replace('__', '_  _')

i_list = find(gift_code, '_')
counter = 1
for i in i_list:
    identifier_string = insert_num(identifier_string, i, counter)
    counter += 1

identifier_string = '           ' + identifier_string
out_string += '\nGift Code: ' + gift_code + '\n' + identifier_string

print(out_string)
