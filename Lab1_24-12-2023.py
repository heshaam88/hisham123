#!/usr/bin/env python
# coding: utf-8

# In[28]:


#####Question 1
x=input("Please Enter a String: ")
vowels = ['a', 'e', 'i', 'o', 'u']
count=0
for char in x.lower():
    if char in vowels :
        count+=1
print(count)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[37]:


#####Question 2
x=[]

for i in range(5):
    number=int(input("Please enter a num.: "))
    x.append(number)

x.sort()
print(x)
#x.reverse()
x.sort(reverse=True)
print(x)


# In[40]:


#####Question 3
x=input("Please enter a string: ")
counter=x.count("the")
print(counter)
#
print(x.count("the"))
#
#


# In[96]:


#####Question 4
x=input("Please enter a string: ")
vowels = ['a', 'e', 'i', 'o', 'u']
y=''
for char in x :
    if not (char  in vowels):
        y= y + char
       
               
print(y)

print(x)


# In[53]:


def remove_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join(char for char in s if char.lower() not in vowels)

s = "your string here"
print(remove_vowels(s))


# In[61]:


#####Question 5
x=input("Please enter a string: ")
places=[]
index=0
for char in x:
    if char =='i':
        places.append(index)
    index+=1

print(places)
print(len(x))


# In[75]:


#####Question 6
num=int(input("Please enter a number: "))

for i in range(1, num+1):
    for j in range(1, num+1):
        if j<=i:
            print(f"{i*j}",end="\t")
   


# In[89]:


#####Question 7
num=int(input("Please enter a number: "))
for i in range(1,num+1):               #lines
    for k in range(num-i+1 , 1 , -1):  #number of spaces in each line
        print(" ",end='')
    for x in range(1,i+1):             #number of * in each line
        print("*",end='')
    print()
    
    
    


# In[ ]:




