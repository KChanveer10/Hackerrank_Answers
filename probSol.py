# 1st Minion's Game - medium - https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# Solution - {Solution is not complete yet}

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



# 2nd question -- (medium level)
# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

# solution

import re
def check(s):  # to check whether integer present in the string or not and to check whether any string is start with integer
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

# 3rd question - Easy - https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true
# solution

s = input("Enter your String: ")
k = int(input("k: "))
d=k
c= len(s)//k
lt=[]
t=0
sol=""
for i in range(c+1):
    x = s[t:k]
    sol = sol+x+"\n"
    t=t+d
    k=k+d
print(sol)

# 4th - easy - https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

n= int(input())
for i in range(n): 
    try:
        int_values = list(map(int, input("").split()))
        c = int_values[0]//int_values[1]
        print(c)
    except ZeroDivisionError as e:
        print(f"Error Code: {e.args[0]}")
    except ValueError as e:
        print(f"Error Code: {e.args[0]}")


# 5th - easy - https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num=nums
        tar = target
        ans= []
        for i in range(len(num)):
            for j in range(len(num)):
                if (num[j]+num[i]==tar):
                    if (i<j):
                        ans.append(i)
                        ans.append(j)
                        return ans

# Pattern Question asked in the Interview 

'''
n = Any odd number (Here n = 7)
Display following output as result
*
**
***
****
***
**
*
'''
# Solution

n=int(input("Enter a odd number: "))
t=n//2
r=n-t
print(t,r)
for i in range(t):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(r):
    for j in range(r-i):
        print("*",end="")
    print()


                
