#! python3

import pyperclip
import re

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?
    (\s|-|\.)?  # separator
    (\d{3})
    (\s|-|\.)?  # separator
    (\d{4})
    (\s*(ext|x|ext.)\s*(\d{2,5}))?
    )''', re.VERBOSE)

# create email regex
email_regex = re.compile(r'''(
    [0-9a-zA-Z._%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    )''', re.VERBOSE)

# find match in clipboard text
text = str(pyperclip.paste())
matches = []
for group in phone_regex.findall(text):
    phone_number = '-'.join([group[1], group[3], group[5]])
    if group[8] != '':
        phone_number += 'x' + group[8]
    matches.append(phone_number)
for groups in email_regex.findall(text):
    # print(groups)
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    # copy 方法只能接收一个字符串 不能接收列表
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone number or email')

# practice in the last
# work 1
# regex = re.compile(r'^(\d{1,3})(,\d{3})*$')
# mo = regex.search('123,23')
# print(mo.group())

# work 2
# regex_name = re.compile(r'^[A-Z][a-zA-Z]*\s[A-Z][a-z]+$')
# mo = regex_name.search('Satoshi Nakamoto')
# print(mo.group())

# work3
# regex3 = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|eats|baseballs)\.', re.IGNORECASE)
# mo2 = regex3.search('BoB eats apples.')
# print(mo2.group())
