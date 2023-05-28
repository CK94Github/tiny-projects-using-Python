# PY_practice
Python_practice
'''salary=int(input("please mention your salary"))

if salary>5:
    print(" necessesry to fill IT returns")
elif salary<5:
    print("not necessery to fill IT returns")
else:
    print ("you can fill Nill return application")'''
    
[test1.txt](https://github.com/CK94Github/PY_practice/files/11071699/test1.txt)
[simple BMI using if_elif.txt](https://github.com/CK94Github/PY_practice/files/11071735/simple.BMI.using.if_elif.txt)


#slpit and replace function:  a="chaitanya kulkarni"
>>> print(a.replace("C","Z"))
chaitanya kulkarni
>>> print(a.replace("c","z"))
zhaitanya kulkarni
>>> b="chaitanaya,kulkarni"
>>> print(b.split (","))
['chaitanaya', 'kulkarni']
>>> b="chaitanya kulkarni"
>>> print(b.split (","))
['chaitanya kulkarni']
>>> print("chaitanya,subhash,kulkarni")
chaitanya,subhash,kulkarni
>>> b="chaitanya,subhash,kulkarni"
>>> print(b.split(","))
['chaitanya', 'subhash', 'kulkarni']

#amstrong number#

i=int(input("enter a numnber"))
arm=i      #since i is changing hance user arm as a veriable 
sum=0
while (i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10

if arm==sum:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")
    
#palindrom number # 

i=int(input("enter a numnber"))
x=i       
rev=0
while (i>0):
    i%10
    rev=(rev*10)+i%10
    i=i//10
if x==rev:
    print("it is an palindrome number")
else:
    print("it is not an palindrome number")
    
    
    #RegEx function..........#######
    
    #regular expression ---RegEx search pattern in string
'''
import re
if re.search('good',"chaitanya is good boy"):
    print("good word is there")

#############################


import re
a=re.findall("good","chaitanya is a good guy in all good guys") #findall multiple times can show pattern
print(a)

for i in a:
    print(i)      #checking how many times good repeated 

###############################################

import re
a="chaitanya is a good guy in all good guys"
for i in re.finditer('good',a):    #finditer will show where both good started and ended 
    b=i.span()                      #convert into touples format
    print(b)'''

#######################################
'''
import re
str='sat,mat,bat,rat,hat,pat,cat'  #random set of strings
a=re.findall('[s,r,c]at',str)   #find related words from str
for i in a:
    print(a)'''


import re
str='sat,mat,bat,rat,hat,pat,cat'  #random set of strings
a=re.findall('[a-k]at',str)   #find related range of words from a-k
for i in a:
    print(a)

