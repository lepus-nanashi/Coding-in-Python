#!/usr/bin/env python
# coding: utf-8

# <h1 style="font-size:3rem;color:orange;">Jupyter Notebook</h1>
# 
# 

# # Python for Beginners

# <h2 style="font-size:2rem;color:cornflowerblue;">Print () Function</h2>
# <text>This function follows the keyword print followed by parentheses, so what is put inside the () goes on the output area
#    

# In[7]:


print("Hello World!")


# <h3 style="font-size:2rem;color:cornflowerblue;">Strings</h3>
# <p> Strings are usually presented between two quotation marks since they are <i>strings</i> of characters</p>
# <text> In the case of cell 8, X is a string of characters which are later printed by the print() function</text>

# In[8]:


x="hello world!!"
print(x)


# <h2 style="font-size:2rem;color:cornflowerblue;">New Line Command</h2>
# <p>Instead of creating multiple new strings for a given text, one can simply use the New Line Command</p>

# In[12]:


print("Hello world \nHello world \nHello World")


# <h2 style="font-size:2rem;color:cornflowerblue;">Concatenation</h2>
# <p>Concatenation is done with the + sign</p>
#            

# In[13]:


print("Hello"+" "+"Natalia")


# <h2 style="font-size:2rem;color:cornflowerblue;">Input () Function</h2>
# <p>This function allows the user of the interface to interact and give data to the program</p>
# <text><i>What is put inside the parentheses is going to be the prompt given to the user</i></text>

# In[16]:


input("Say something ")


# In[18]:


print("Hello, " + input ("What is your name?")+"!")


# In[22]:


print("want to know how long is your name?")
x=input("What is your name? ")
print(len(x))


# <h1 style="font-size:3rem;color:cornflowerblue;">Variables</h1>

# In[24]:


name= input("what is your name? ")
print("Hello, "+name)


# <p>Allows to refer to previous data when it is named</p>
# <p>However, the variable can later on be modified in another line of code</p>

# In[25]:


name="natalia"
print(name)
name="nana"
print(name)


# In[28]:


name=input("what is your name? ")
length=len(name)
print(length)


# <h1 style="font-size:4;color:orange;">Band Name Generator!</h1>

# In[33]:


print("You want to form a band, but don't know how to name it?\nSay no more!")
first_name=input("What is your name?\n")
first_pet_name=input("What was your first pet's name?\n")
print("Your band name could be "+first_name+" "+first_pet_name)


# In[ ]:




