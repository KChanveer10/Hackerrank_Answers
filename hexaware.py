# # input_str = input("enter your string: ")
# # hyphens=''
# # non_hyphens=''
# # for char in input_str:
# #     if char =="-":
# #         hyphens = hyphens+char
# #     else:
# #         non_hyphens = non_hyphens+char
# # print(hyphens+non_hyphens)


# import string
# import random
 
# # initializing size of string
# N = 7
 
# # using random.choices()
# # generating random strings
# input_Str = ''.join(random.choices(string.ascii_letters, k=N))
# first = input_Str[0]  # first element stored in var
# indfir = []  # to keep the track of the indexes of first var
# indsec = []  # to keep the track of the indexes of second var

# # for loop that append the indexes of first element
# for i in range(len(input_Str)):
#     if first == input_Str[i]:
#         indfir.append(i)


# # to find the second char if first element is repeated
# def second_char(input_Str):
#     second = ""
#     for i in range(len(input_Str)):
#         if input_Str[i] == input_Str[i + 1]:
#             continue
#         else:
#             second = input_Str[i + 1]
#             break
#     return second


# second = second_char(input_Str)

# # for loop that append indexes of the second element
# for i in range(len(input_Str)):
#     if second == input_Str[i]:
#         indsec.append(i)

# print(first,"->",indfir)
# print(second,"->",indsec)

# newstr = list(input_Str)

# # following code is responsible for swapping of the elements

# for k in indfir:
#     newstr[k] = second
# for j in indsec:
#     newstr[j] = first

# ans =''
# for i in newstr:
#     ans = ans+i
# print(input_Str)
# print(ans)

#3 https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

# s = input("Enter your String: ")
# k = int(input("k: "))
# d=k
# c= len(s)//k
# print(d)
# lt=[]
# t=0
# for i in range(c):
#     x = s[t:k]
#     lt.append(x)
#     t=t+d
#     k=k+d
# print(lt)


# cool=[]
# for i in lt:
#     l = set()
#     for j in range(len(i)):
#         l.add(i[j])
#     cool.append(l)
# print(cool)


# # email-id: mttestacc7@gmail.com




# input_str="1222311"

# list1 = list(input_str)
# strlist= set()
# for i in list1:
#     strlist.add(i)
# list2=list(strlist)
# list2.sort()
# num=[]
# oc=[]

# for i in range(len(list2)):
#     n=list2[i]
#     i=0
#     for j in list1:
#         if n == j:
#             i=i+1
#     num.append(int(n))
#     oc.append(i)
# for i in range(len(num)):
#     print(((oc[i]),(num[i])))

# print(num)
# print(oc)

# import math

# ab = 1
# bc = 10

# ac = math.sqrt((ab**2+bc**2))

# print("ac ->",ac)
# mc = ac/2
# print("mc ->",mc)


# bm =mc
# print("bm ->",bm)



# angle = (bc**2+bm**2-mc**2)/(2*bc*bm)

# print("angle ->",angle)

# result = math.acos(angle)*(180*7/22)
# print(result)
# print(str(round(result))+chr(176))

# import math

# ab = 1
# bc = 10

# ac = math.sqrt((ab**2+bc**2))
# # b = ac/2

# # c =(ab*bc)/ac

# # m=bc

# result = math.acos((ab**2+bc**2-ac**2)/(2*ab*bc))*(180.0/math.pi)
# result = result/2
# print(str(round(result))+chr(176))





# s = input("Enter a String: ")
# vowels=[]
# consonants=[]
# indvo= []
# indco = []
# for i in range(len(s)):
#     if (s[i] == "A" or s[i]=='E' or s[i] == 'I' or s[i]=='O' or s[i]=='U'):
#         vowels.append(s[i])
#         indvo.append(i)
#     else:
#         consonants.append(s[i])
#         indco.append(i)


# for i in range(len(vowels)):
#     key = vowels[i]
#     value = indvo[i]
#     if key not in vowels_dict:
#         vowels_dict[key]=value 

# for i in range(len(consonants)):
#     key = consonants[i]
#     value = indco[i]
#     if key not in const_dict:
#         const_dict[key]=value            

# print(vowels_dict)
# print(const_dict)

vowels_dict = {}
const_dict = {}

for i, char in enumerate(s):
    if char.upper() in "AEIOU":
        if char not in vowels_dict:
            vowels_dict[char] = [i]
        else:
            vowels_dict[char].append(i)
    else:
        if char not in const_dict:
            const_dict[char] = [i]
        else:
            const_dict[char].append(i)

print("Vowels Dictionary:", vowels_dict)
print("Consonants Dictionary:", const_dict)


vow_score =0
for i in vowels_dict:
    lst = vowels_dict[i]
    for k in range(len(lst)):
        newstr=''
        for j in range(lst[k],len(s)):
            sr=0
            newstr = newstr +s[j]
            for k in range(len(s)):
                c = s[k:k+len(newstr)]
                if newstr ==c:
                    vow_score = vow_score+1
                    sr = sr + 1
            print(f"{newstr}->{sr}")  
            

con_score =0

for i in const_dict:
    lst = const_dict[i]
    for k in range(len(lst)):
        newstr=""
        for j in range(lst[k],len(s)):
            sr=0
            newstr = newstr +s[j]
            for k in range(len(s)):
                c = s[k:k+len(newstr)]
                if newstr ==c:
                    con_score = con_score+1
                    sr = sr + 1
            print(f"{newstr}->{sr}")
        

if vow_score>con_score:
    print(f"Kevin {vow_score}")
else:
    print(f"Stuart {con_score}") 