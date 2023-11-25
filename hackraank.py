s = input("Enter your string: ")
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