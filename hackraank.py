# s = input("Enter your string: ")
# vowels_dict = {}
# const_dict = {}

# for i, char in enumerate(s):
#     if char.upper() in "AEIOU":
#         if char not in vowels_dict:
#             vowels_dict[char] = [i]
#         else:
#             vowels_dict[char].append(i)
#     else:
#         if char not in const_dict:
#             const_dict[char] = [i]
#         else:
#             const_dict[char].append(i)

# print("Vowels Dictionary:", vowels_dict)
# print("Consonants Dictionary:", const_dict)


# vow_score =0
# for i in vowels_dict:
#     lst = vowels_dict[i]
#     for k in range(len(lst)):
#         newstr=''
#         for j in range(lst[k],len(s)):
#             sr=0
#             newstr = newstr +s[j]
#             for k in range(len(s)):
#                 c = s[k:k+len(newstr)]
#                 if newstr ==c:
#                     vow_score = vow_score+1
#                     sr = sr + 1
#             print(f"{newstr}->{sr}")  
            

# con_score =0

# for i in const_dict:
#     lst = const_dict[i]
#     for k in range(len(lst)):
#         newstr=""
#         for j in range(lst[k],len(s)):
#             sr=0
#             newstr = newstr +s[j]
#             for k in range(len(s)):
#                 c = s[k:k+len(newstr)]
#                 if newstr ==c:
#                     con_score = con_score+1
#                     sr = sr + 1
#             print(f"{newstr}->{sr}")
        

# if vow_score>con_score:
#     print(f"Kevin {vow_score}")
# else:
#     print(f"Stuart {con_score}") 



# 2nd question -- (medium level)
# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

# # solution

import re
def check(s):
    regex = '^\d+$|^\d+[a-zA-Z]$'
    if(re.search(regex, s)):
        return 1
    else:
        return 0

def solve():
    s = input("Enter your String: ")
    s = s.split(" ")
    ne_sp=[]
    # print(chr(32))
    for i in s:
        l = check(i)
        if i=='':
            ne_sp.append(' ')
        elif(l):
            ne_sp.append(i)
            ne_sp.append(' ')
        else:
            x = i[0]
            n = ord(x)
            if n>=65 and n<97:
                n = n
            else:
                n = n - 32
            x = chr(n) + i[1:]
            ne_sp.append(x)
            ne_sp.append(' ')

    x=""
    for i in range(0,len(ne_sp)-1):
        x = x+ne_sp[i]
    return x

result = solve()         
print(result)