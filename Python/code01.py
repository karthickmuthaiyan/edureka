def factor(n):
    for i in range(1,num+1):
        if num % i== 0: 
            print(i,end=" ")
            if i%2==0:
                print(' is an even number')
            else:
                print(' is an odd number')

num=int(input('Enter the num:'))
print('Factors of number', num,'are:')
factor(num)
    

++++++++++++++++++++++++++++++++++++++++++++++++++

# find reverse of string

def f_palindrome(v_str):
    i=len(v_str)
    string=v_str
    reverse=''
    while i > 0:
        #print(v_str[i-1])
        #print(v_str[:-1])
        reverse+=v_str[i-1]
        v_str=v_str[:-1]
        #print(v_str)
        i=i-1
    if reverse == string :
        print('String: ',string,' is a palindrome')
    else:
        print('String: ',string,' is not a palindrome')
    #print(reverse)
    

i=input('Enter Stirng')
f_palindrome(i)


+++++++++++++++++++++++++++++++++++++++++
# Find palindrome

string=input()
if string == string[::-1]:
    print (string,' is a palindrome')
else:
    print (string,' is not a palindrome')

# Find digits alphabets & sort 

v_string=set(input("Enter the string"))
num_cnt=0
str_cnt=0
num_str=''
str_str=''
for str in v_string:
    #print(str)
    if str.isdigit():
        #print('number is:',str)
        num_cnt+=1
        num_str+=str
    elif str.isalpha(): 
        #print('string is:',str)
        str_cnt+=1
        str_str+=str
#print('Alphabets are:',str_str,',Numbers are:',' is ', num_str)
#sorted_str=''.join(sorted(v_string,key=str.lower))

sorted_word = ''.join(sorted(v_string, key=lambda x: x.lower()))
print(sorted_word)

+++++++++++++++++++++++++++++++++++++++
# Sort word with blank spaces
# Sort a Python String with sorted()
word = 'da kk %%!ta ?gy!'
sorted_word = ''.join( sorted(filter(lambda x:x.isalpha(),word),key=lambda x:x.lower()))
print(sorted_word)
# Returns: aadgty

+++++++++++++++++++++++++++++++++++++++=

#Sort words 
#string = "Hi My name is Karthick"
string=input("Enter words")
v_words=' '.join(sorted(string.split()))
print(v_words)

++++++++++++++++++++++++++++++++++++++++++++++

# Find valid number between 3000 to 4000 with even 

v_numbers=input("Enter numbers separated by space")
for num in v_numbers.split():
    if int(num) >= 3000 and int(num) <=4000 :
        if int(num) %2 == 0:
            print(num, ' is valid and even')
        else:
            print(num, ' is valid but not even')
    else:
        print(num, ' is not valid')

++++++++++++++++++++++++++++++++++++++++++++++++++++

# Password verification

password=input("Enter Password")
ctr_alpha=0
ctr_spl=0
ctr_digit=0
ctr_lower=0
for ltr in password:
    if ltr.isalpha():
        ctr_alpha+=1
        if ltr.islower():
            ctr_lower+=1
    if ltr.isdigit():
        ctr_digit+=1
    if ltr in '$#@':
        ctr_spl+=1

if ctr_alpha >=1 and ctr_spl >=1 and  ctr_alpha >=1 and ctr_lower >=1 and ctr_alpha+ctr_spl+ctr_alpha >=6 and  ctr_alpha+ctr_spl+ctr_alpha <=12:
    print('Success, this is a valid password')
else:
    print("Password validation failed")

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Find value of string and positions

a = [4,7,3,2,5,9]
for val in range(1,len(a)+1):
    print('In position', val ,' is ', a[val-1])

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Print even indexes
str=input("Enter String")
print(str[::2])

str=input("Enter String")
o_str=""
for x in str:
    if x.isalpha():
        o_str+=x
print(o_str)

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# reverse the input string

str=input("Enter String")
print(str[::-1])

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Count occurence of uniq characters

str=input("Enter String")

for x in sorted(set(str)):
    print(x,',',str.count(x,0,len(str)))

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Interseciton of two lists

a=[1,3,6,78,35,55,88]
b=[12,24,35,24,88,120,155]
c=[]
for i in a:
    if i in b:
        c.append(i)
print(c)

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Remove duplicate lines without changing order 

dup_list=input("Eneter numbers")
unique_list=[]
for num in dup_list.split(","):
    print(num)
    if num not in unique_list:
        unique_list.append(num)
print (unique_list)

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Print list after removing 24 
lst=[12,24,35,24,88,120,155]
lst.pop(1)
print(lst)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Print after removing 0,4th and 5th elements

lst=[12,24,35,24,88,120,155]
for i in 5,4,0:
    lst.pop(i)
print(lst)

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Pop numbers from list divisible by 5 & 7 

lst=[12,24,35,70,88,120,155]
lst1=[]
for i in range(0,len(lst)):
    print(lst[i])
    if lst[i]%5 == 0 and lst[i]%7 == 0 :
        pass
    else:
        lst1.append(lst[i])
lst=lst1
print(lst) 

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Random numbers between 1 and 1000 inclusive and divisible by 5 & 7 

import random
print (random.sample([i for i in range(1,1001) if i%5==0 and i%7==0 ],5))

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# Find 1/2+2/3+..n/n+1 for n > 0 

import sys
n=input("Enter number")
sum=float(0)
if int(n) > 0:
  print ("A +ve integer")
else:
  print ("Not a +ve integer")
  sys.exit(1) 
for i in range(1, int(n) + 1 ):
    #print (i)
    sum=sum + (i / (i+1))
print ('%.2f'%sum)  


