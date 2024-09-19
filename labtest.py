#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data=np.array(["Lion","Elephant","Zebra"])
time=np.array([1,2,3,4,5,6,7,8,9,10])
lion=np.array([15,16,17,20,19,21,23,24,25,27])
elephant=np.array([50,52,54,53,55,56,57,59,60,62])
zebra=np.array([100,98,95,97,96,94,95,93,92,90])


# In[3]:


total_lion=sum(lion)
total_elephant=sum(elephant)
total_zebra=sum(zebra)

print("Total lions:",total_lion)
print("Total elephnats:",total_elephant)
print("Total zebras:",total_zebra)
print("Average yearly growth of lions:",total_lion/10)
print("Average yearly growth of elephants:",total_elephant/10)
print("Average yearly growth of zebras:",total_zebra/10)


# In[4]:


totalLions=0
for i in range (0,10):
    totalLions=totalLions+lion[i]
    lion[i]=totalLions/(i+1)
    print("Growth in year",i+1,"of lions is",totalLions/(i+1))


# In[5]:


totalElephants=0
for i in range (0,10):
    totalElephants=totalElephants+elephant[i]
    elephant[i]=totalElephants/(i+1)
    print("Growth in year ",i+1," of lions is",totalElephants/(i+1))


# In[6]:


totalZebras=0
for i in range (0,10):
    totalZebras=totalZebras+zebra[i]
    zebra[i]=totalZebras/(i+1)
    print("Growth in year ",i+1," of lions is",totalZebras/(i+1))


# In[7]:


plt.plot(time,lion,label="Lion",color='r')
plt.plot(time,elephant,label="Elephant",color='g')
plt.plot(time,zebra,label="Zebra",color='b')
plt.title("Population Trend")
plt.xlabel("Animals")
plt.ylabel("Years")
plt.legend()
plt.show()


# In[8]:


growth=np.array([total_lion,total_elephant,total_zebra])
for i in range (0,3):
    for j in range (0,3):
        if growth[i]<growth[j]:
            temp=growth[i]
            growth[i]=growth[j]
            growth[j]=temp
            temp=data[i]
            data[i]=data[j]
            data[j]=temp
            


print(data[2],"has the highest growth rate of",growth[2]/10)


# In[9]:


plt.bar(1,total_lion,label="lions",linewidth=0.1)
plt.bar(2,total_elephant,label="elephants",linewidth=0.1)
plt.bar(3,total_zebra,label="zebras",linewidth=0.1)
plt.legend()
plt.title("Total population at end of 10 years")
plt.xlabel("After 10 years")
plt.ylabel("Growth")
plt.show()


# In[ ]:




